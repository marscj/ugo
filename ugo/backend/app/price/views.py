from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from middleware.viewsets import CustomModelViewSet
from .models import Price
from .serializers import PriceSerializer

class PriceView(CustomModelViewSet):
    serializer_class = PriceSerializer
    queryset = Price.objects.all()
    permission_classes = [IsAuthenticated]