from rest_framework import  serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import ProductImage

class ProductImageSerializer(serializers.ModelSerializer):

    product = serializers.PrimaryKeyRelatedField(required=False, allow_null=True, read_only=True)
    # product = ProductSerializer(required=False, allow_null=True, read_only=True)

    product_id = serializers.IntegerField(write_only=True)

    image = VersatileImageFieldSerializer(required=False, allow_null=True, sizes='product_size')

    class Meta:
        model = ProductImage
        fields = '__all__'