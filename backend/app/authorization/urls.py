from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'user', views.UserView, basename='user')
router.register(r'role', views.RoleView, basename='role')
router.register(r'permission', views.PermissionView, basename='permission')
router.register(r'action', views.ActionEntityView, basename='action')

urlpatterns = [
    url(r'auth/login', views.LoginJwtTokenView.as_view(), name='login'),
    url(r'auth/logout', views.LogoutJwtTokenView.as_view(), name='logout'),
    url(r'admin/login', views.StaffLoginJwtTokenView.as_view(), name='adminlogin'),
]

urlpatterns = urlpatterns + router.urls