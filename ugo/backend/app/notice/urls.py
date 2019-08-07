from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'notice', views.NoticeView, basename='notice')
router.register(r'system_notice', views.NoticeReadOnlyView, basename='system_notice')

urlpatterns = router.urls