from django.db import models

from versatileimagefield.fields import VersatileImageField

class Category(models.Model):

    name = models.CharField(blank=True, null=True, max_length=16, unique=True)

    class Meta:
        db_table = 'category'

class Product(models.Model):

    name = models.CharField(blank=True, null=True, max_length=128, unique=True)

    description = models.CharField(blank=True, null=True, max_length=128)

    image = VersatileImageField(upload_to="products", blank=False)
    
    category = models.ForeignKey(Category, blank=True, null=True, related_name='product', on_delete=models.SET_NULL)

    class Meta:
        db_table = 'product'

class ProductVariant(models.Model):

    sku = models.CharField(max_length=32, unique=True)

    name = models.CharField(blank=True, null=True, max_length=128, unique=True)

    description = models.CharField(blank=True, null=True, max_length=128)

    product = models.ForeignKey(Product, blank=True, null=True, related_name='variant', on_delete=models.CASCADE)

    images = models.ManyToManyField("ProductImage", blank=True)

    class Meta:
        db_table = 'productvariant'

class ProductImage(models.Model):

    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )

    image = VersatileImageField(upload_to="products", blank=False)

    class Meta:
        db_table = 'productimage'

    def get_ordering_queryset(self):
        return self.product.images.all()