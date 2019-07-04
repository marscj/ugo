from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Category, Product, ProductVariant
from .serializers import CategorySerializer, ProductSerializer, ProductVariantSerializer

class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        print(response.data)
        response.data = {
            'result': response.data
        }
        print(response.data)
        return response


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().cache()

class ProductVariantView(ModelViewSet):
    serializer_class = ProductVariantSerializer
    queryset = ProductVariant.objects.all().cache()

