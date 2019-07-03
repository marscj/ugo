from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Product, ProductVariant
from .serializers import ProductSerializer, ProductVariantSerializer

class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().cache()

class ProductVariantView(ModelViewSet):
    serializer_class = ProductVariantSerializer
    queryset = ProductVariant.objects.all().cache()

