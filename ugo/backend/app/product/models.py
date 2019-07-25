from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.postgres.fields import ArrayField, DecimalRangeField

from app.source.models import ProductImage

from .import Category

class Product(models.Model):

    status = models.BooleanField(default=True)

    category = models.IntegerField(default=Category.Food, choices=Category.CHOISE)

    productID = models.CharField(blank=True, null=True, max_length=16, unique=True)

    name = models.CharField(blank=True, null=True, max_length=128, unique=True)

    description = models.CharField(blank=True, null=True, max_length=128)

    subtitle = models.TextField(blank=True, null=True)

    location = models.CharField(blank=True, null=True, max_length=32)
    
    content = models.TextField(blank=True, null=True)

    photo = models.ForeignKey(ProductImage, blank=True, null=True, related_name='photo', on_delete=models.SET_NULL)

    gallery = models.ManyToManyField(ProductImage, blank=True, related_name='gallery')

    class Meta:
        db_table = 'product'

class ProductVariant(models.Model):

    status = models.BooleanField(default=True)

    variantID = models.CharField(blank=True, null=True, max_length=16, unique=True)

    name = models.CharField(blank=True, null=True, max_length=64, unique=True)

    sku = models.CharField(max_length=32, unique=True)

    adult_status = models.BooleanField(default=True)
    
    adult_desc = models.CharField(blank=True, null=True, max_length=64)

    adult_quantity = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    adult_price = ArrayField(models.DecimalField(max_digits=10, decimal_places=2), size=5)

    child_status = models.BooleanField(default=False)

    child_desc = models.CharField(blank=True, null=True, max_length=64)

    child_quantity = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    child_price = ArrayField(models.DecimalField(max_digits=10, decimal_places=2), size=5)

    product = models.ForeignKey(Product, blank=True, null=True, related_name='variant', on_delete=models.CASCADE)

    class Meta:
        db_table = 'variant'

    @property
    def category(self):
        return self.product.category

