from django.apps import AppConfig

class OrderConfig(AppConfig):
    name = 'app.order'

    def ready(self):
        from .import handle