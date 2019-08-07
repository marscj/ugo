from middleware.viewsets import CustomModelViewSet
from middleware.permissions import MiddlewarePermission
from rest_framework.permissions import AllowAny

from .models import Notice
from .serializers import NoticeSerializer

class NoticeView(CustomModelViewSet):
    serializer_class = NoticeSerializer
    permission_classes = [MiddlewarePermission]
    queryset = Notice.objects.all()

class NoticeReadOnlyView(CustomModelViewSet):
    serializer_class = NoticeSerializer
    permission_classes = [AllowAny]
    queryset = Notice.objects.all()