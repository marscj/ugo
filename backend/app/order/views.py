from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
import django_filters

from middleware.viewsets import CustomModelViewSet
from middleware.permissions import MiddlewarePermission
from .models import Order
from .serializers import OrderCreateSerializer, OrderUpdateSerializer, OrderBackendUpdateSerializer, CheckoutSerializer
from app.product.models import ProductVariant
from app.authorization.models import CustomUser

class OrderFilter(django_filters.FilterSet):
    customer_id = django_filters.NumberFilter('customer_id')
    operator_id = django_filters.NumberFilter('operator_id')
    product_id = django_filters.NumberFilter('product_id')
    variant_id = django_filters.NumberFilter('variant_id')
    order_status = django_filters.NumberFilter('order_status')
    pay_status = django_filters.NumberFilter('pay_status')
    start_day = django_filters.DateFilter('day',lookup_expr=('gte'),) 
    end_day = django_filters.DateFilter('day',lookup_expr=('lte'))

class OrderView(CustomModelViewSet):
    serializer_class = OrderCreateSerializer
    permission_classes = [MiddlewarePermission]
    queryset = Order.objects.all()

    permissionId = Order.__name__
 
    filterset_fields = ('day', 'order_status', 'pay_status', 'customer_id', 'operator_id', 'product_id' , 'variant_id')
    filter_class = OrderFilter

    search_fields = (
        'orderID',
        'confirmID',
        'variant',
        'product',
        'customer',
        'operator',
    )

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        else:
            if self.request.user.is_staff:
                return OrderBackendUpdateSerializer
            else:
                return OrderUpdateSerializer

    @action(detail=False, methods=['post'], permission_classes=[MiddlewarePermission])
    def checkout(self, request):
        checkout = CheckoutSerializer(data=request.data, context={'request': request})
        if checkout.is_valid(raise_exception=True):
            data = checkout.data
            return Response({
                'result': data
            })
