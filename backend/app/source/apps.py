from django.apps import AppConfig


class SourceConfig(AppConfig):
    name = 'app.source'

    def ready(self):
        from .import handle