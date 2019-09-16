from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
import django_filters

from middleware.viewsets import CustomModelViewSet
from middleware.permissions import BackendPermission
from .models import Order
from .serializers import OrderCreateSerializer, OrderUpdateSerializer, CheckoutSerializer
from app.product.models import ProductVariant
from app.authorization.models import CustomUser

class OrderFilter(django_filters.FilterSet):
    order_status = django_filters.NumberFilter('order_status')
    pay_status = django_filters.NumberFilter('pay_status')
    start_day = django_filters.DateFilter('day',lookup_expr=('gte'),) 
    end_day = django_filters.DateFilter('day',lookup_expr=('lte'))
    
    orderID = django_filters.CharFilter('orderID')
    variant = django_filters.CharFilter('variant')
    product = django_filters.CharFilter('product')
    customer = django_filters.CharFilter('customer')
    operator = django_filters.CharFilter('operator')

class OrderView(CustomModelViewSet):
    serializer_class = OrderCreateSerializer
    permission_classes = [BackendPermission]
    queryset = Order.objects.all()

    permissionId = Order.__name__
 
    filterset_fields = ('day', 'order_status', 'pay_status', 'orderID', 'variant', 'product', 'customer', 'operator')
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
