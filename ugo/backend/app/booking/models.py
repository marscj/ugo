from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

from app.product.models import ProductVariant

class Booking(models.Model):

    # 预定号
    bookingId = models.CharField(blank=True, null=True, max_length=32, unique=True)

    # 确认号
    confirmId = models.CharField(blank=True, null=True, max_length=64, unique=True)

    day = models.DateField(blank=True, null=True)

    startTime = models.TimeField(blank=True, null=True)

    endTime = models.TimeField(blank=True, null=True)

    createAt = models.DateTimeField(auto_now_add=True)

    changeAt = models.DateTimeField(auto_now=True)

    adultQuantity = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    childQuantity = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    product = models.ForeignKey(ProductVariant, blank=True, null=True, related_name='booking', on_delete=models.CASCADE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='booking', on_delete=models.SET_NULL)

    remark = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'booking'