from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from middleware.viewsets import CustomModelViewSet
from middleware.permissions import MiddlewarePermission, ReadOnlyPermission
from .models import Category, Product, ProductVariant
from .serializers import (ProductListSerializer, ProductDetailSerializer, ProductDetailReadOnlySerializer, ProductVariantSerializer, ProductVariantReadOnlySerializer)

class ProductView(CustomModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [MiddlewarePermission]

    permissionId = Product.__name__

    filterset_fields = ('category', 'status')
    search_fields = ('title', 'productID')

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        else:
            return ProductDetailSerializer

    # @action(methods=['delete'], detail=False)
    # def multiple_delete(self, request,  *args, **kwargs):
    #     delete_id = request.query_params.get('deleteid', None)
    #     if not delete_id:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     for i in delete_id.split(','):
    #         get_object_or_404(User, pk=int(i)).delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class ProductReadOnlyView(CustomModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [ReadOnlyPermission]

    filterset_fields = ('category', 'status')
    search_fields = ('title', )

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        else:
            return ProductDetailReadOnlySerializer
 
class ProductVariantView(CustomModelViewSet): 
    serializer_class = ProductVariantSerializer
    permission_classes = [MiddlewarePermission]
    queryset = ProductVariant.objects.all()

    filterset_fields = ('product__category', 'status')
    search_fields = ('variantID', 'sku', 'name', 'product__title')
    
    permissionId = Product.__name__

class ProductVariantReadOnlyView(CustomModelViewSet): 
    serializer_class = ProductVariantReadOnlySerializer
    queryset = ProductVariant.objects.all()
    permission_classes = [ReadOnlyPermission]