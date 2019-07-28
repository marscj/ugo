from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from middleware.viewsets import CustomModelViewSet
from .models import Order
from .serializers import OrderSerializer
from app.authorization import UserType

class OrderView(CustomModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [AllowAny]

    filterset_fields = ('day', )
    search_fields = ('orderID', )

    def perform_update(self, serializer):
        if serializer.validated_data.get('operator_id', None) is None:
            if self.request.user.user_type is not None and self.request.user.user_type == UserType.Staff:
                serializer.save(operator=self.request.user)
        
        return super().perform_update(serializer)