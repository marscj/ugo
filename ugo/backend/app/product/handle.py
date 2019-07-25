# from django.dispatch import receiver
# from django.db.models.signals import post_save, pre_save, pre_delete, post_delete

# from .models import ProductVariant
# from app.authorization import UserType
# from app.price.models import Price
# from app.authorization.models import CustomUser

# @receiver(post_save, sender=ProductVariant)
# def product_model_post_save(sender, instance, created, **kwargs):
#     if created:
#         for user in CustomUser.objects.filter(user_type=UserType.Company):
#             Price.objects.create(variant=instance, user=user)

