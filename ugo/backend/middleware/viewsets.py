from rest_framework.viewsets import ModelViewSet

class ModelViewSetMixin(object):

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'result': response.data
        }
        return response

class CustomModelViewSet(ModelViewSetMixin, ModelViewSet):
    pass

