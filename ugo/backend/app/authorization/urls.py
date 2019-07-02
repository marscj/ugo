from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'user', views.UserView, basename='user')
router.register(r'role', views.RoleView, basename='role')

urlpatterns = [
    url(r'auth/login', views.LoginJwtTokenView.as_view(), name='login'),
    url(r'auth/logout', views.LogoutJwtTokenView.as_view(), name='logout'),
]

urlpatterns = urlpatterns + router.urls