from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete

from .models import Product

@receiver(pre_delete, sender=Product)
def product_model_post_delete(sender, instance, **kwargs):

    if instance.photo is not None: 
        instance.photo.delete()
    
    if instance.gallery is not None:
        instance.gallery.all().delete()

