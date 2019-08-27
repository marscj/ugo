from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from middleware.viewsets import CustomModelViewSet
from middleware.permissions import BackendOrSafePermission
from .models import Category, Product, ProductVariant
from .serializers import (ProductListSerializer, ProductSerializer, ProductBackendSerializer, 
    ProductVariantSerializer, ProductVariantBackendSerializer)

class ProductView(CustomModelViewSet):
    queryset = Product.objects.all().cache()
    serializer_class = ProductSerializer
    permission_classes = [BackendOrSafePermission]

    permissionId = Product.__name__

    filterset_fields = ('category', 'status')
    search_fields = ('title', 'productID')
    ordering_fields = ('id', 'sort_by')

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.request.user.is_staff:
                return ProductBackendSerializer
        return ProductSerializer

    @action(methods=['delete'], detail=False, permission_classes=[BackendOrSafePermission])
    def delete(self, request,  *args, **kwargs):
        ids = request.query_params.get('ids', None)
        
        if not ids:
            return Response({'message': 'Not Found!'}, status=status.HTTP_400_BAD_REQUEST)
        
        for i in ids.split(','):
            try:
                Product.objects.get(pk=int(i)).delete()
            except Product.DoesNotExist:
                return Response({
                'message': 'Not Found!'
            })

        return Response({'result': 'ok'})

    @action(methods=['post'], detail=False, permission_classes=[BackendOrSafePermission])
    def enable(self, request,  *args, **kwargs):
        ids = request.query_params.get('ids', None)
        enable = request.query_params.get('enable', 0)
        
        if not ids:
            return Response({'message': 'Not Found!'}, status=status.HTTP_400_BAD_REQUEST)
        
        for i in ids.split(','):
            try:
                product = Product.objects.get(pk=int(i))
                product.status = enable
                product.save()
            except Product.DoesNotExist:
                return Response({'message': 'Not Found!'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'result': 'ok'})
 
class ProductVariantView(CustomModelViewSet): 
    queryset = ProductVariant.objects.all().cache()
    serializer_class = ProductVariantSerializer
    permission_classes = [BackendOrSafePermission]

    filterset_fields = ('product__category', 'status')
    search_fields = ('variantID', 'sku', 'name', 'product__title')
    ordering_fields = ('id', 'sort_by')
    
    permissionId = Product.__name__

    def get_serializer_class(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return ProductVariantBackendSerializer
        return ProductVariantSerializer

    @action(methods=['delete'], detail=False, permission_classes=[BackendOrSafePermission])
    def delete(self, request,  *args, **kwargs):
        ids = request.query_params.get('ids', None)
        
        if not ids:
            return Response({'message': 'Not Found!'}, status=status.HTTP_400_BAD_REQUEST)
        
        for i in ids.split(','):
            try:
                ProductVariant.objects.get(pk=int(i)).delete()
            except ProductVariant.DoesNotExist:
                return Response({
                'message': 'Not Found!'
            })

        return Response({'result': 'ok'})

    @action(methods=['post'], detail=False, permission_classes=[BackendOrSafePermission])
    def enable(self, request,  *args, **kwargs):
        ids = request.query_params.get('ids', None)
        enable = request.query_params.get('enable', 0)
        
        if not ids:
            return Response({'message': 'Not Found!'}, status=status.HTTP_400_BAD_REQUEST)
        
        for i in ids.split(','):
            try:
                product = ProductVariant.objects.get(pk=int(i))
                product.adult_status = enable
                product.status = enable
                product.save()
            except ProductVariant.DoesNotExist:
                return Response({'message': 'Not Found!'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'result': 'ok'})