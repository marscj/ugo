from django.db import models
import uuid

from .import PaymentStatus
from app.order.models import Order

class Payment(models.Model):
    total = models.DecimalField(max_digits=9, decimal_places=2, default='0.0')
    currency = models.CharField(max_length=10, default='USD')
    status = models.CharField(max_length=10, choices=PaymentStatus.CHOICES, default=PaymentStatus.FULLY_PAID)
    extra_data = models.TextField(blank=True, default='')
    token = models.CharField(max_length=36, blank=True, default=uuid.uuid4())
    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, default='')

    order = models.ForeignKey(Order, on_delete=models.SET_NULL, related_name='payment', blank=True, null=True)

    class Meta:
        db_table = 'payment'
        ordering = ['-id']