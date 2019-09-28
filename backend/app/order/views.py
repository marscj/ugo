from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction
from django.db.models import Sum, Q
from  decimal import Decimal
import django_filters

from django.core.exceptions import ValidationError


from middleware.viewsets import CustomModelViewSet
from middleware.permissions import BackendPermission
from .models import Order
from .serializers import OrderCreateSerializer, OrderUpdateSerializer, CheckoutSerializer

from app.payment.models import Payment
from app.payment import PaymentAction, PaymentStatus

class OrderFilter(django_filters.FilterSet):
    order_status = django_filters.NumberFilter('order_status')
    start_day = django_filters.DateFilter('day',lookup_expr=('gte'),) 
    end_day = django_filters.DateFilter('day',lookup_expr=('lte'))
    
    orderID = django_filters.CharFilter('orderID')
    relatedID = django_filters.CharFilter('relatedID')
    variant = django_filters.CharFilter('variant')
    product = django_filters.CharFilter('product')
    customer = django_filters.CharFilter('customer')
    customer_id = django_filters.NumberFilter('customer_id')
    operator = django_filters.CharFilter('operator')
    operator_id = django_filters.NumberFilter('operator_id')
    
class OrderView(CustomModelViewSet):
    serializer_class = OrderCreateSerializer
    permission_classes = [BackendPermission]
    queryset = Order.objects.all()

    permissionId = Order.__name__
 
    filterset_fields = ('day', 'order_status', 'orderID', 'relatedID' 'variant', 'product', 'customer', 'customer_id', 'operator',  'operator_id')
    filter_class = OrderFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        else:
            return OrderUpdateSerializer

    @action(detail=False, methods=['post'], permission_classes=[BackendPermission])
    def checkout(self, request):
        checkout = CheckoutSerializer(data=request.data, context={'request': request})
        if checkout.is_valid(raise_exception=True):
            return Response({
                'result': checkout.data
            })
            
    @transaction.atomic
    @action(detail=True, methods=['put'], permission_classes=[BackendPermission])
    def refund(self, request, pk=None):
        amount = request.data.get('amount', None)
        description = request.data.get('description', '')

        if amount:
            amount = Decimal(amount)
            order = self.get_object()
            
            if amount <= 0:
                return Response({
                    'message': {'amount': '退款金额必须大于0.'}
                }, status=400)
            
            if amount > order.total:
                return Response({
                    'message': {'amount': '退款金额必须小于订单总金额.'}
                }, status=400)

            total = Payment.objects.filter(
                Q(order_id=order.id) & Q(status=PaymentStatus.REFUNDING) & Q(action=PaymentAction.REFUNDED)
            ).aggregate(sum=Sum('total'))['sum'] or 0.0

            if amount > order.total - Decimal(total):
                return Response({
                    'message': {'amount': '申请的退款总金额已大于订单金额.'}
                }, status=400)

            order.refund(amount, description)

            return Response({'result': 'ok'})

        else:
            return Response({
                'message': {'amount': '请输入退款金额.'}
            }, status=400)