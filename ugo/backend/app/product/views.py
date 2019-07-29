from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from middleware.viewsets import CustomModelViewSet
from .models import Category, Product, ProductVariant
from .serializers import ProductSerializer, ProductDetailSerializer, ProductVariantSerializer

class ProductView(CustomModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [AllowAny]

    filterset_fields = ('category', 'status')
    search_fields = ('title', )

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer
        else:
            return ProductDetailSerializer
 
class ProductVariantView(CustomModelViewSet):
    serializer_class = ProductVariantSerializer
    queryset = ProductVariant.objects.all()
    permission_classes = [AllowAny]