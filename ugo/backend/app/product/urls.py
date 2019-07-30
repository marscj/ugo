from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'product', views.ProductReadOnlyView, basename='product')
router.register(r'variant', views.ProductVariantReadOnlyView, basename='variant')
router.register(r'system_product', views.ProductView, basename='product')
router.register(r'system_variant', views.ProductVariantView, basename='product')

urlpatterns = router.urls