from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from middleware.viewsets import CustomModelViewSet
from .models import Order
from .serializers import OrderSerializer

class ProductView(CustomModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [AllowAny]

    filterset_fields = ('day', )
    search_fields = ('orderID', )