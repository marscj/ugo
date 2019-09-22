from django.db import models
from django.utils.crypto import get_random_string
from django.core.validators import MinValueValidator

from app.product.models import ProductVariant
from app.authorization.models import CustomUser

class Coupon(models.Model):
    couponID = models.CharField(blank=True, null=True, max_length=16)
    enable = models.BooleanField(default=True)
    amount = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    exp_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='coupon')
    customer = models.ManyToManyField(CustomUser, related_name='coupon')

    class Meta:
        db_table = 'coupon'
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if not self.couponID:
            while True:
                couponID = get_random_string(length=8)
                if not self.__class__._default_manager.filter(couponID=couponID).exists():
                    self.couponID = couponID
                    break

        super(Coupon, self).save(*args, **kwargs)