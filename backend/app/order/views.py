from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
import django_filters

from middleware.viewsets import CustomModelViewSet
from middleware.permissions import MiddlewarePermission
from .models import Order
from .serializers import OrderCreateSerializer, OrderUpdateSerializer, CheckoutOrderSerializer
from app.product.models import ProductVariant
from app.authorization.models import CustomUser

class OrderFilter(django_filters.FilterSet):
    customer_id = django_filters.NumberFilter('customer__id')
    order_status = django_filters.NumberFilter('order_status')
    pay_status = django_filters.NumberFilter('pay_status')
    start_day = django_filters.DateFilter('day',lookup_expr=('gte'),) 
    end_day = django_filters.DateFilter('day',lookup_expr=('lte'))

class OrderView(CustomModelViewSet):
    serializer_class = OrderCreateSerializer
    permission_classes = [MiddlewarePermission]
    queryset = Order.objects.all()

    permissionId = Order.__name__
 
    filterset_fields = ('day', 'order_status', 'pay_status', 'customer_id')
    filter_class = OrderFilter

    search_fields = (
        'orderID',
        'confirmID',
        'variant__name',
        'variant__product__title',
        'customer__username',
        'operator__username',
    ) 

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        else:
            return OrderUpdateSerializer

    @action(detail=False, methods=['post'])
    def checkout(self, request):
        checkout = CheckoutOrderSerializer(data=request.data, context={'request': request})
        if checkout.is_valid(raise_exception=True):
            data = checkout.data
            data.update({
                'total_price': checkout._get_total_price(checkout.data),
                'product': checkout.variant.product.title,
                'variant': checkout.variant.name
            })
            return Response({
                'result': data
            })
