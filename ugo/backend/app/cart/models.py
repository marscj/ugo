from django.db import models
from django.core.validators import MinValueValidator

from app.product.models import ProductVariant

class Cart(models.Model):
    
    day = models.DateField(blank=True, null=True)

    startTime = models.TimeField(blank=True, null=True)

    endTime = models.TimeField(blank=True, null=True)

    createAt = models.DateTimeField(auto_now_add=True)

    changeAt = models.DateTimeField(auto_now=True)

    adultQuantity = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    childQuantity = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    product = models.ForeignKey(ProductVariant, blank=True, null=True, related_name='cart', on_delete=models.CASCADE)

    remark = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'cart'