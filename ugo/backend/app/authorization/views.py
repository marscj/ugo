from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken

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