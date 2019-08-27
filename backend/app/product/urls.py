from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'product', views.ProductView, basename='product')
router.register(r'variant', views.VariantView, basename='variant')

urlpatterns = router.urls