from django.db import models
from django.conf import settings

from app.product.models import ProductVariant

class UserPrice(models.Model):

    variant = models.ForeignKey(ProductVariant, related_name='price', on_delete=models.CASCADE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='price', on_delete=models.CASCADE)
