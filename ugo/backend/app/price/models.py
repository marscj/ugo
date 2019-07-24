from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from app.product.models import ProductVariant

class Price(models.Model):

    variant = models.ForeignKey(ProductVariant, related_name='price', on_delete=models.CASCADE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='price', on_delete=models.CASCADE)

    curLev = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    lv1 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    lv2 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    lv3 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    lv4 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    lv5 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    class Meta:
        db_table = 'price'