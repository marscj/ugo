from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from middleware.viewsets import CustomModelViewSet
from .models import Category, Product, ProductVariant
from .serializers import ProductSerializer, ProductVariantSerializer #CategorySerializer, 

# class CategoryView(CustomModelViewSet):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()

class ProductView(CustomModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
 
class ProductVariantView(CustomModelViewSet):
    serializer_class = ProductVariantSerializer
    queryset = ProductVariant.objects.all()