from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import FileUploadParser

from django.core.files.uploadedfile import UploadedFile

from middleware.viewsets import CustomModelViewSet
from .models import Category, Product, ProductVariant
from .serializers import CategorySerializer, ProductSerializer, ProductVariantSerializer

class CategoryView(CustomModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ProductView(CustomModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().cache()
 
class ProductVariantView(CustomModelViewSet):
    serializer_class = ProductVariantSerializer
    queryset = ProductVariant.objects.all().cache()

class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        return Response(status=204)