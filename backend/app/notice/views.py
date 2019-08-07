from middleware.viewsets import CustomModelViewSet
from middleware.permissions import MiddlewarePermission, ReadOnlyPermission

from .models import Notice
from .serializers import NoticeSerializer, NoticeReadOnlySerializer

class NoticeView(CustomModelViewSet):
    serializer_class = NoticeSerializer
    permission_classes = [MiddlewarePermission]
    queryset = Notice.objects.all()

    permissionId = Notice.__name__

class NoticeReadOnlyView(CustomModelViewSet):
    serializer_class = NoticeReadOnlySerializer
    permission_classes = [ReadOnlyPermission]
    queryset = Notice.objects.all()