import uuid
import hashlib
from django.db import models
from django.core.validators import MinValueValidator

from .import OrderStatus, PayStatus
from app.product.models import ProductVariant
from app.authorization.models import CustomUser

def create_uuid():
    return '%019d' % uuid.uuid4().__hash__()

class Order(models.Model):
    
    #订单ID
    orderID = models.CharField(default=create_uuid, max_length=64)

    #确认号
    confirmID = models.CharField(blank=True, null=True, max_length=64)

    #订单状态
    order_status = models.IntegerField(default=OrderStatus.CREATE, choices=OrderStatus.CHOICE)

    #支付状态
    pay_status = models.IntegerField(default=PayStatus.UNPAID, choices=PayStatus.CHOICE)

    #日期
    day = models.DateField()

    #时间
    time = models.TimeField()

    #创建于
    create_at = models.DateTimeField(auto_now_add=True)

    #修改于
    change_at = models.DateTimeField(auto_now=True)

    #客户信息
    guest_info = models.TextField(blank=True, null=True)

    #客户联系方式
    guest_contact = models.TextField(blank=True, null=True)

    #成人票数量
    adult_quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    #成人票金额
    adult_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    #儿童票数量
    child_quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    #儿童票金额
    child_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    #总金额
    total_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    #备注
    remark = models.TextField(blank=True, null=True)

    #主产品名称
    product = models.CharField(default=create_uuid, max_length=128)

    #子产品名称
    variant = models.CharField(default=create_uuid, max_length=64)

    #主产品ID
    productID = models.CharField(blank=True, null=True, max_length=16, unique=True)

    #子产品ID
    variantID = models.CharField(blank=True, null=True, max_length=16, unique=True)

    #sku
    models.CharField(max_length=32, unique=True)

    #客户username
    customer = models.CharField(blank=True, null=True, max_length=150)

    #客户ID
    customer_id = models.IntegerField(blank=True, null=True)

    #操作username
    operator = models.CharField(blank=True, null=True, max_length=150)

    #操作ID
    operator_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.orderID