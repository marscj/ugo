from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from middleware.viewsets import CustomModelViewSet
from .models import ProductImage, HomeContent
from .serializers import ProductImageSerializer, HomeContentSerializer

class ProductImageView(CustomModelViewSet):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()
    
class HomeContentView(APIView):
    
    def get(self, request, format=None):
        serializer = HomeContentSerializer(data=HomeContent.objects.get(pk=1))
        return Response({'result': serializer.data})

    def post(self, request, format=None):
        serializer = HomeContentSerializer(data=request.POST)
        serializer.save()
        return Response({'result': serializer.data})

    def update(self, request, format=None):
        serializer = HomeContentSerializer(data=request.POST)
        serializer.save()
        return Response({'result': serializer.data})
    