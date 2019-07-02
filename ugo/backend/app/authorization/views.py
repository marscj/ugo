from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework_jwt.views import ObtainJSONWebToken

from .models import CustomUser, Role, Permission, ActionEntity
from .serializers import UserSerializer, RoleSerializer, PermissionSerializer, ActionEntitySerializer

class LoginJwtTokenView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        print(request.data)
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            return response
        else:
            return Response({'message': 'Unable to log in with provided credentials.'}, status=response.status_code)

class LogoutJwtTokenView(APIView):

    def post(self, request, *args, **kwargs):
        return Response({'ok'})

class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all().cache()

    @action(detail=False, methods=['get'])
    def info(self, request):
        serializer = self.get_serializer(request.user)
        context = {
            'code': 20000,
            'result': serializer.data
        }
        return Response(context)

class RoleView(ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all().cache()

class PermissionView(ModelViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all().cache()