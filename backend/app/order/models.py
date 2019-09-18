import uuid
import hashlib
from django.db import models
from django.core.validators import MinValueValidator

from .import OrderStatus
from app.product import Category

def create_uuid():
    return '%019d' % uuid.uuid4().__hash__()

class Order(models.Model):
    
    #订单ID
    orderID = models.CharField(blank=True, null=True, max_length=64)

    #订单状态
    order_status = models.IntegerField(default=OrderStatus.CREATE, choices=OrderStatus.CHOICE)

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

    #客户备注
    guest_remark = models.TextField(blank=True, null=True)

    #成人票数量
    adult_quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    #成人票金额
    adult_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    #成人单价
    adult_unit_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    #儿童票数量
    child_quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    #儿童单价
    child_unit_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    #儿童票金额
    child_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    #总金额
    total = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    #订单备注
    remark = models.TextField(blank=True, null=True)

    #主产品名称
    product = models.CharField(blank=True, null=True, max_length=128)

    #子产品名称
    variant = models.CharField(blank=True, null=True, max_length=64)

    #主产品ID
    productID = models.CharField(blank=True, null=True, max_length=16)

    #子产品ID
    variantID = models.CharField(blank=True, null=True, max_length=16)

    #产品分类
    category = models.IntegerField(default=Category.Food, choices=Category.CHOISE)

    #sku
    sku = models.CharField(blank=True, null=True, max_length=32)

    #客户username
    customer = models.CharField(blank=True, null=True, max_length=150)

    #客户ID
    customer_id = models.IntegerField(blank=True, null=True)

    #操作username
    operator = models.CharField(blank=True, null=True, max_length=150)

    #操作ID
    operator_id = models.IntegerField(blank=True, null=True)

    #逻辑删除
    is_delete = models.BooleanField(default=False)

    #来自于
    order_from = models.CharField(default='ugodubai', blank=True, null=True, max_length=64)

    class Meta:
        db_table = 'order'
        ordering = ['-id']

    def __str__(self):
        return self.orderID

        
            
        