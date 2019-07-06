from django.db import models

class Category(models.Model):

    name = models.CharField(blank=True, null=True, max_length=16, unique=True)

    class Meta:
        db_table = 'category'

class Product(models.Model):

    productID = models.CharField(blank=True, null=True, max_length=16, unique=True)

    name = models.CharField(blank=True, null=True, max_length=128, unique=True)

    description = models.CharField(blank=True, null=True, max_length=128)
    
    content = models.TextField(blank=True, null=True)

    category = models.ForeignKey(Category, blank=True, null=True, related_name='product', on_delete=models.SET_NULL)

    class Meta:
        db_table = 'product'

class ProductVariant(models.Model):

    productID = models.CharField(blank=True, null=True, max_length=16, unique=True)

    sku = models.CharField(max_length=32, unique=True)

    name = models.CharField(blank=True, null=True, max_length=128, unique=True)

    description = models.CharField(blank=True, null=True, max_length=128)

    product = models.ForeignKey(Product, blank=True, null=True, related_name='variant', on_delete=models.CASCADE)

    class Meta:
        db_table = 'productvariant'