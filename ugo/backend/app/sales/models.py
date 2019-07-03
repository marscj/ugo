from django.db import models
from django.core.validators import MinValueValidator

from app.product.models import ProductVariant

class Sales(models.Model):

    online = models.BooleanField(default=True)
    
    adultQuantity = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    childQuantity = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    product = models.ForeignKey(ProductVariant, blank=True, null=True, related_name='sales', on_delete=models.CASCADE)

    class Meta:
        db_table = 'sales'
