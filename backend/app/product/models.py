from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.postgres.fields import ArrayField, DecimalRangeField

from app.source.models import ProductImage

from .import Category

class Product(models.Model):

    status = models.BooleanField(default=True)

    category = models.IntegerField(default=Category.Food, choices=Category.CHOISE)

    productID = models.CharField(blank=True, null=True, max_length=16, unique=True)

    title = models.CharField(blank=True, null=True, max_length=128, unique=True)

    subtitle = models.CharField(blank=True, null=True, max_length=2048)

    special = models.TextField(blank=True, null=True)

    location = models.CharField(blank=True, null=True, max_length=32)
    
    content = models.TextField(blank=True, null=True)

    photo = models.ForeignKey(ProductImage, blank=True, null=True, related_name='photo', on_delete=models.SET_NULL)

    gallery = models.ManyToManyField(ProductImage, blank=True, related_name='gallery')

    # sort_by = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.title

class ProductVariant(models.Model):

    status = models.BooleanField(default=True)

    variantID = models.CharField(blank=True, null=True, max_length=16, unique=True)

    name = models.CharField(blank=True, null=True, max_length=64)

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

    # sort_by = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        db_table = 'variant'

    def __str__(self):
        return self.name

