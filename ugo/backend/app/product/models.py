from django.db import models

from versatileimagefield.fields import PPOIField, VersatileImageField

class Category(models.Model):

    name = models.CharField(blank=True, null=True, max_length=16)

    class Meta:
        db_table = 'category'

class CategoryTranslation(models.Model):
    code = models.CharField(blank=True, null=True, max_length=16)

    category = models.ForeignKey(Category, blank=True, null=True, related_name='translation', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categorytranslation'

class Product(models.Model):

    name = models.CharField(blank=True, null=True, max_length=128)

    description = models.CharField(blank=True, null=True, max_length=128)

    image = VersatileImageField(upload_to="products", ppoi_field="ppoi", blank=False)
    
    category = models.ForeignKey(Category, blank=True, null=True, related_name='product', on_delete=models.SET_NULL)

    class Meta:
        db_table = 'product'

class ProductTranslation(models.Model):

    code = models.CharField(blank=True, null=True, max_length=16)

    product = models.ForeignKey(Product, blank=True, null=True, related_name='translation', on_delete=models.CASCADE)

    class Meta:
        db_table = 'producttranslation'

class ProductVariant(models.Model):

    sku = models.CharField(max_length=32, unique=True)

    name = models.CharField(blank=True, null=True, max_length=128)

    description = models.CharField(blank=True, null=True, max_length=128)

    product = models.ForeignKey(Product, blank=True, null=True, related_name='variant', on_delete=models.CASCADE)

    images = models.ManyToManyField("ProductImage", through="VariantImage")

    class Meta:
        db_table = 'productvariant'
    
class ProductVariantTranslation(models.Model):

    code = models.CharField(blank=True, null=True, max_length=16)

    productvariant = models.ForeignKey(ProductVariant, blank=True, null=True, related_name='translation', on_delete=models.CASCADE)

    class Meta:
        db_table = 'productvarianttranslation'

class ProductImage(models.Model):

    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )

    image = VersatileImageField(upload_to="products", ppoi_field="ppoi", blank=False)

    ppoi = PPOIField()

    alt = models.CharField(max_length=128, blank=True)

    class Meta:
        db_table = 'productimage'

    def get_ordering_queryset(self):
        return self.product.images.all()


class VariantImage(models.Model):

    variant = models.ForeignKey(
        "ProductVariant", related_name="variant_images", on_delete=models.CASCADE
    )

    image = models.ForeignKey(
        ProductImage, related_name="variant_images", on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'variantimage'