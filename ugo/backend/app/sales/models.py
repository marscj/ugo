from django.db import models
from django.core.validators import MinValueValidator

from app.product.models import ProductVariant

class Sales(models.Model):

    online = models.BooleanField(default=True)
    
    adultQuantity = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    childQuantity = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    child_ticket_desc = models.CharField(blank=True, null=True, max_length=64)

    adultPrice = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    childPrice = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    variant = models.ForeignKey(ProductVariant, blank=True, null=True, related_name='sales', on_delete=models.CASCADE)

    class Meta:
        db_table = 'sales'
