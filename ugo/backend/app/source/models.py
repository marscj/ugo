from django.db import models
from uuid import uuid4

from versatileimagefield.fields import VersatileImageField, PPOIField

from app.product.models import Product

class ProductImage(models.Model):

    uid = models.UUIDField(default=uuid4)

    flag = models.CharField(blank=True, null=True, max_length=16)

    description = models.CharField(blank=True, null=True, max_length=64)

    image = VersatileImageField(blank=True, null=True, upload_to='products/', ppoi_field='image_ppoi',)
    
    image_ppoi = PPOIField()

    product = models.ForeignKey(Product, blank=True, null=True, related_name="image", on_delete=models.CASCADE)

    class Meta:
        db_table = 'source'

    def get_ordering_queryset(self):
        return self.product.images.all()
