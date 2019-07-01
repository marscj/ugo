from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken

class LoginJwtTokenView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class LogoutJwtTokenView(APIView):

    def post(self, request, *args, **kwargs):
        return Response({'ok'})