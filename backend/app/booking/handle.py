from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete

from .models import Booking

@receiver(post_save, sender=Booking)
def booking_model_post_save(sender, instance, created, **kwargs):
    if created:
        if instance.bookingID is None or instance.bookingID == '':
            instance.bookingID = str(instance.id + 1000000000)
            instance.save()
        