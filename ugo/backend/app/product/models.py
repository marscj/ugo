from django.db import models

from app.source.models import ProductImage

from .import Category

# class Category(models.Model):

#     name = models.CharField(blank=True, null=True, max_length=16, unique=True)

#     class Meta:
#         db_table = 'category'

class Product(models.Model):

    category = models.IntegerField(default=Category.Food, choices=Category.CHOISE)

    productID = models.CharField(blank=True, null=True, max_length=16, unique=True)

    name = models.CharField(blank=True, null=True, max_length=128, unique=True)

    description = models.CharField(blank=True, null=True, max_length=128)

    subtitle = models.TextField(blank=True, null=True)

    location = models.CharField(blank=True, null=True, max_length=32)
    
    content = models.TextField(blank=True, null=True)

    photo = models.ForeignKey(ProductImage, blank=True, null=True, related_name='photo', on_delete=models.SET_NULL)

    gallery = models.ManyToManyField(ProductImage, blank=True, related_name='gallery')

    # category = models.ForeignKey(Category, blank=True, null=True, related_name='product', on_delete=models.SET_NULL)

    class Meta:
        db_table = 'product'

class ProductVariant(models.Model):

    variantID = models.CharField(blank=True, null=True, max_length=16, unique=True)

    sku = models.CharField(max_length=32, unique=True)

    name = models.CharField(blank=True, null=True, max_length=128, unique=True)

    product = models.ForeignKey(Product, blank=True, null=True, related_name='variant', on_delete=models.CASCADE)

    class Meta:
        db_table = 'productvariant'

    @property
    def category(self):
        return self.product.category