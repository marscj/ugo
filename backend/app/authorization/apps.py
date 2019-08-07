from django.apps import AppConfig


class AuthorizationConfig(AppConfig):
    name = 'app.authorization'

    def ready(self):
        from .import handle