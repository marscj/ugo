from rest_framework.permissions import IsAuthenticatedOrReadOnly

from middleware.viewsets import CustomModelViewSet
from middleware.permissions import BackendOrSafePermission

from .models import Notice
from .serializers import NoticeSerializer, NoticeReadOnlySerializer

class NoticeView(CustomModelViewSet):
    serializer_class = NoticeSerializer
    permission_classes = [BackendOrSafePermission]
    queryset = Notice.objects.all()

    permissionId = Notice.__name__