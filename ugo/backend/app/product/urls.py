from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'category', views.CategoryView, basename='product')
router.register(r'product', views.ProductView, basename='product')
router.register(r'productvariant', views.ProductVariantView, basename='productvariant')
router.register(r'image', views.ProductImageView, base_name='images')

urlpatterns = [
    url(r'upload', views.FileUploadView.as_view(), name='upload'),
]

urlpatterns = urlpatterns + router.urls