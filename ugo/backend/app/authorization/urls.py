from django.conf.urls import url, include

from .import views

urlpatterns = [
    url(r'auth/login', views.LoginJwtTokenView.as_view(), name='login'),
    url(r'auth/logout', views.LogoutJwtTokenView.as_view(), name='logout'),
]