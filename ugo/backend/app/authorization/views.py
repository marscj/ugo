from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework_jwt.views import ObtainJSONWebToken

from middleware.viewsets import CustomModelViewSet
from .models import CustomUser, Role, Permission, ActionEntity
from .serializers import UserSerializer, RoleSerializer, PermissionSerializer, ActionEntitySerializer

class LoginJwtTokenView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            return response
        else:
            return Response({'message': 'Unable to log in with provided credentials.'}, status=response.status_code)

class LogoutJwtTokenView(APIView):

    def post(self, request, *args, **kwargs):
        return Response({'ok'})

class UserView(CustomModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all().cache()

class RoleView(CustomModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all().cache()

class PermissionView(CustomModelViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all().cache()

class ActionEntityView(CustomModelViewSet):
    serializer_class = ActionEntitySerializer
    queryset = ActionEntity.objects.all().cache()