from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from middleware.viewsets import CustomModelViewSet
from .models import Order
from .serializers import OrderSerializer
from app.product.models import ProductVariant
from app.authorization.models import CustomUser
from app.authorization import UserType

class OrderView(CustomModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [AllowAny]
 
    filterset_fields = ('day', )
    search_fields = ('orderID', )

    @action(detail=False, methods=['post'])
    def checkout(self, request):
        print(request.data)
        checkout = self.get_serializer(data=request.data)
        if checkout.is_valid(raise_exception=True):
            info = checkout.get_info(checkout.data)
            return Response({'result': {
                'day': checkout.data['day'],
                'time': checkout.data['time'],
                'customer_info': checkout.data['customer_info'],
                'customer_contact': checkout.data['customer_contact'],
                'adult_quantity': checkout.data['adult_quantity'],
                'adult_price': info['adult_price'],
                'child_quantity': checkout.data['child_quantity'],
                'child_price': info['child_price'],
                'remark': checkout.data['remark'],
                'variant': info['variant'].__str__(),
                'variant_id': checkout.data['variant_id'],
            }})
