from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction
import django_filters

from middleware.viewsets import CustomModelViewSet
from middleware.permissions import BackendPermission

from .models import Booking
from .serializers import BookingSerializer

class OrderFilter(django_filters.FilterSet):
    bookingID = django_filters.CharFilter('bookingID')
    orderID = django_filters.CharFilter('order_id')
    booking_start_day = django_filters.DateFilter('booking_date',lookup_expr=('gte'),) 
    booking_end_day = django_filters.DateFilter('booking_date',lookup_expr=('lte'))
    action_start_day = django_filters.DateFilter('action_date',lookup_expr=('gte'),) 
    action_end_day = django_filters.DateFilter('action_date',lookup_expr=('lte'))
    guide = django_filters.CharFilter('guide')
    driver = django_filters.CharFilter('driver')
    vehicle = django_filters.CharFilter('vehicle')
    officer = django_filters.CharFilter('officer')
    operator = django_filters.CharFilter('operator')
    status = django_filters.NumberFilter('status')
    category = django_filters.NumberFilter('category')

class BookingView(CustomModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [BackendPermission]
    queryset = Booking.objects.all()

    permissionId = Booking.__name__

    filterset_fields = ('bookingID', 'orderID', 'booking_start_day', 'booking_end_day',
     'action_start_day', 'action_end_day', 'guide', 'driver', 'vehicle',  'officer', 'operator', 'status', 'category')
    filter_class = OrderFilter
    search_fields = ('product', )