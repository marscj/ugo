from django.db import models
from django.core.validators import MinValueValidator

from app.product.models import Category

from . import BookingStatus, MealPeriod

class Booking(models.Model):

    #预定id
    bookingID = models.CharField(blank=True, null=True, max_length=64)

    #团id
    groupID = models.CharField(blank=True, null=True, max_length=64)
    
    #下单日期
    booking_date = models.DateField(blank=True, null=True)

    #执行日期
    action_day = models.DateField(blank=True, null=True)

    #执行时间
    action_time = models.TimeField(blank=True, null=True)

    #产品
    product = models.CharField(blank=True, null=True, max_length=128)
    
    #子产品
    variant = models.CharField(blank=True, null=True, max_length=64)

    #用餐
    meal = models.IntegerField(default=MealPeriod.LUNCH, choices=MealPeriod.CHOICE)

    #产品类型
    category = models.IntegerField(default=Category.Food, choices=Category.CHOISE)

    #成人数量
    adult_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    #儿童数量
    child_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    #免费数量
    free_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    #成人价格 USD
    adult_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    #儿童价格 USD
    child_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    #总价 USD
    total_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    #成人成本价 AED
    adult_cost_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    #儿童成本价 AED
    child_cost_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    #总价成本价 AED
    total_cost_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    #税务 AED
    vat = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    #确认好
    ref = models.TextField(blank=True, null=True)

    #接送时间
    pick_up_time = models.DateTimeField(blank=True, null=True)

    #接送地址
    pick_up_address = models.CharField(blank=True, null=True, max_length=256)

    #接送地址
    drop_off_address = models.CharField(blank=True, null=True, max_length=256)

    #司机
    driver = models.CharField(blank=True, null=True, max_length=150)

    #司机电话
    driver_mobile = models.CharField(blank=True, null=True, max_length=150)

    #车型
    vehicle_model = models.CharField(blank=True, null=True, max_length=64)

    #车牌号
    vehicle_number = models.CharField(blank=True, null=True, max_length=64)

    #导游
    guide = models.CharField(blank=True, null=True, max_length=150)

    #导游电话
    guide_mobile = models.CharField(blank=True, null=True, max_length=16)

    #操作
    operator = models.CharField(blank=True, null=True, max_length=150)

    #预定
    officer = models.CharField(blank=True, null=True, max_length=150)

    #状态
    status = models.IntegerField(default=BookingStatus.INQUIRY, choices=BookingStatus.CHOICE)

    #备注
    remark = models.TextField(blank=True, null=True)

    #创建时间
    create_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    #修改时间
    change_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    #供应商
    supplier = models.CharField(blank=True, null=True, max_length=64)

    #订单id
    order_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'booking'
        ordering = ['-id']