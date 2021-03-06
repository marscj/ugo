from rest_framework.viewsets import ModelViewSet

class ModelViewSetMixin(object):

    permissionId = 'None'

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'result': response.data
        }
        return response

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {
            'result': response.data
        }
        return response

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.data = {
            'result': response.data
        }
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data = {
            'result': response.data
        }
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data = {
            'result': 'ok'
        }
        response.status_code = 200
        return response

class CustomModelViewSet(ModelViewSetMixin, ModelViewSet):
    pass

