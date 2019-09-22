
from rest_framework.response import Response
import django_filters

from middleware.viewsets import CustomModelViewSet
from middleware.permissions import BackendPermission

from .models import Coupon
from .serializers import CouponSerializer
from app.product.models import Product
    
class CouponView(CustomModelViewSet):
    serializer_class = CouponSerializer
    permission_classes = [BackendPermission]
    queryset = Coupon.objects.all()

    permissionId = Product.__name__
 
    filterset_fields = ('couponID')