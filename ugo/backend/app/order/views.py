from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from middleware.viewsets import CustomModelViewSet
from .models import Order
from .serializers import OrderSerializer, CheckoutOrderSerializer
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
        checkout = CheckoutOrderSerializer(data=request.data, context={'request': request})
        if checkout.is_valid(raise_exception=True):
            data = checkout.data
            data.update({
                'product': checkout.variant.product.title,
                'variant': checkout.variant.name
            })
            return Response({
                'result': data
            })
