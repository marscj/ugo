from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction

from middleware.viewsets import CustomModelViewSet
from middleware.permissions import BackendPermission

from .models import Booking
from .serializers import BookingSerializer
    
class BookingView(CustomModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [BackendPermission]
    queryset = Booking.objects.all()

    permissionId = Booking.__name__