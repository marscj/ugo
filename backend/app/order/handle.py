from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete

from .models import Order

@receiver(post_save, sender=Order)
def order_model_post_save(sender, instance, created, **kwargs):
    if created:
        if instance.orderID is None or instance.orderID == '':
            instance.orderID = str(instance.id + 1000000000)
            instance.save()
        