from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete

from .models import ProductVariant
from app.authorization import UserType
from app.price.models import Price
from app.authorization.models import CustomUser

from app.price.models import Price
from app.product.models import ProductVariant


