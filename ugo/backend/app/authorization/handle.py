from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete

from .models import Role, Permission, ActionEntity

# @receiver(post_save, sender=Role)
# def role_model_post_save(sender, instance, created, **kwargs):
#     if created:
#         pass
        