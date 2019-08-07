from django.apps import AppConfig


class ProductConfig(AppConfig):
    name = 'app.product'

    def ready(self):
        from .import handle