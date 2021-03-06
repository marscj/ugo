from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'coupon', views.CouponView, basename='coupon')

urlpatterns = router.urls