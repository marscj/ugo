from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete

from .models import ProductImage

@receiver(post_delete, sender=ProductImage)
def source_model_post_delete(sender, instance, **kwargs):
    instance.image.delete_all_created_images()
    instance.image.delete(save=False)

