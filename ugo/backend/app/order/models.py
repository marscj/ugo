from django.db import models
from django.core.validators import MinValueValidator

from .import OrderStatus
from app.product.models import ProductVariant
from app.authorization.models import CustomUser

class Order(models.Model):
    
    orderID = models.CharField(blank=True, max_length=32)

    confirmID = models.CharField(blank=True, null=True, max_length=64)

    order_status = models.IntegerField(default=OrderStatus.CREATE, choices=OrderStatus.CHOICE)

    day = models.DateField()

    time = models.TimeField()

    create_at = models.DateTimeField(auto_now_add=True)

    change_at = models.DateTimeField(auto_now=True)

    customer_contact = models.TextField(blank=True, null=True)

    customer_info = models.TextField(blank=True, null=True)

    adult_quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    adult_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    child_quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    child_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    remark = models.TextField(blank=True, null=True)

    variant = models.ForeignKey(ProductVariant, related_name='order', on_delete=models.SET_NULL, null=True)

    customer = models.ForeignKey(CustomUser, related_name='order_custom', on_delete=models.SET_NULL, blank=True, null=True)

    operator = models.ForeignKey(CustomUser, related_name='order_operator', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'order'

    @property
    def total_price(self):
        return self.adult_price + child_price