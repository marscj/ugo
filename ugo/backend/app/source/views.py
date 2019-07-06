from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from middleware.viewsets import CustomModelViewSet
from .models import ProductImage
from .serializers import ProductImageSerializer

class ProductImageView(CustomModelViewSet):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()
