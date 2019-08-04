from rest_framework.viewsets import ModelViewSet

class ModelViewSetMixin(object):

    permissionId = 'None'

    def list(self, request, *args, **kwargs):
        print(request)
        print(request.data)
        response = super().list(request, *args, **kwargs)
        response.data = {
            'result': response.data
        }
        print(response.data)
        return response

    def create(self, request, *args, **kwargs):
        print(request)
        print(request.headers)
        print(request.data)
        response = super().create(request, *args, **kwargs)
        response.data = {
            'result': response.data
        }
        print(response.data)
        return response

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.data = {
            'result': response.data
        }
        print(response.data)
        return response

    def update(self, request, *args, **kwargs):
        # print(request.data)
        response = super().update(request, *args, **kwargs)
        response.data = {
            'result': response.data
        }
        # print(response.data)
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data = {
            'result': 'ok'
        }
        response.status_code = 200
        print(response.data)
        return response

class CustomModelViewSet(ModelViewSetMixin, ModelViewSet):
    pass

