from django.apps import AppConfig


class BookingConfig(AppConfig):
    name = 'app.booking'

    def ready(self):
        from .import handle