from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.settings import api_settings

from .import UserType
from middleware.viewsets import CustomModelViewSet
from middleware.permissions import MiddlewarePermission, MiddlewareLoginPermission
from .models import CustomUser, Role, Permission, ActionEntity
from .serializers import UserSerializer, UserCreateSerializer, ChangePasswordSerializer, UserSimpleSerializer, RoleSerializer, PermissionSerializer, ActionEntitySerializer

class LoginJwtTokenView(ObtainJSONWebToken):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == 200:
            return response
        else:
            return Response({
                'message': {'detail': '用户名或者密码错误.'}
            }, status=response.status_code)

class StaffLoginJwtTokenView(ObtainJSONWebToken):
    permission_classes = [MiddlewareLoginPermission]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            return response
        else:
            return Response({
                'message': {'detail': '用户名或者密码错误.'}
            }, status=response.status_code)

class LogoutJwtTokenView(APIView):
    def post(self, request, *args, **kwargs):
        response = Response({'ok'})
        if api_settings.JWT_AUTH_COOKIE:
            response.delete_cookie(api_settings.JWT_AUTH_COOKIE)
        return response

class UserView(CustomModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [MiddlewarePermission]
    queryset = CustomUser.objects.all().cache()

    permissionId = CustomUser.__name__
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        else:
            return UserSerializer

    def get_current_user(self):
        return self.request.user

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def info(self, request):
        serializer = self.get_serializer(request.user)
        context = { 
            'result': serializer.data
        }
        return Response(context)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def change_password(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            self.get_current_user().set_password(serializer.data.get('new_password'))
            self.get_current_user().save()
            return Response({'result': 'ok'})

class RoleView(CustomModelViewSet):
    serializer_class = RoleSerializer
    permission_classes = [MiddlewarePermission]
    queryset = Role.objects.all().order_by('-id').cache()

    permissionId = Role.__name__

class PermissionView(CustomModelViewSet):
    serializer_class = PermissionSerializer
    permission_classes = [MiddlewarePermission]
    queryset = Permission.objects.all().cache()

    permissionId = Role.__name__

class ActionEntityView(CustomModelViewSet):
    serializer_class = ActionEntitySerializer
    permission_classes = [MiddlewarePermission]
    queryset = ActionEntity.objects.all().cache()

    permissionId = Role.__name__