from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.postgres.fields import ArrayField, DecimalRangeField

from app.source.models import ProductImage

from .import Category

#主产品
class Product(models.Model):

    #主产品状态
    status = models.BooleanField(default=True)

    #主产品分类
    category = models.IntegerField(default=Category.Food, choices=Category.CHOISE)

    #主产品ID
    productID = models.CharField(blank=True, null=True, max_length=16, unique=True)

    #主产品名称
    title = models.CharField(blank=True, null=True, max_length=128, unique=True)

    #主产品副标题
    subtitle = models.CharField(blank=True, null=True, max_length=2048)

    #主产品特色
    special = models.TextField(blank=True, null=True)

    #主产品地点
    location = models.CharField(blank=True, null=True, max_length=32)
    
    #主产品内容
    content = models.TextField(blank=True, null=True)

    #主产品icon
    photo = models.ForeignKey(ProductImage, blank=True, null=True, related_name='photo', on_delete=models.SET_NULL)

    #主产品走马灯
    gallery = models.ManyToManyField(ProductImage, blank=True, related_name='gallery')

    #主产品排序
    sort_by = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        db_table = 'product'
        ordering = ['-id']

    def __str__(self):
        return self.title

#子产品
class ProductVariant(models.Model):

    #子产品状态
    status = models.BooleanField(default=True)

    #子产品ID
    variantID = models.CharField(blank=True, null=True, max_length=16, unique=True)

    #子产品名称
    name = models.CharField(blank=True, null=True, max_length=64)

    #子产品sku
    sku = models.CharField(blank=True, null=True, max_length=32, unique=True)

    #子产品成人票状态
    adult_status = models.BooleanField(default=True)
    
    #子产品成人票说明
    adult_desc = models.CharField(blank=True, null=True, max_length=64)

    #子产品成人票数量
    adult_quantity = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    #子产品成人票价格
    adult_price = ArrayField(models.DecimalField(max_digits=10, decimal_places=2), size=5)

    #子产品儿童票状态
    child_status = models.BooleanField(default=False)

    #子产品儿童票说明
    child_desc = models.CharField(blank=True, null=True, max_length=64)

    #子产品儿童票数量
    child_quantity = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    #子产品儿童票价格
    child_price = ArrayField(models.DecimalField(max_digits=10, decimal_places=2), size=5)

    #主产品ID
    product = models.ForeignKey(Product, blank=True, null=True, related_name='variant', on_delete=models.CASCADE)

    #子产品排序
    sort_by = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        db_table = 'variant'
        ordering = ['-id']

    def __str__(self):
        return self.name