from rest_framework import  serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import ProductImage, HomeContent

class ProductImageSerializer(serializers.ModelSerializer):

    # product = serializers.PrimaryKeyRelatedField(required=False, allow_null=True, read_only=True)
    # product = ProductSerializer(required=False, allow_null=True, read_only=True)

    # product_id = serializers.IntegerField(required=False, allow_null=True, write_only=True)

    image = VersatileImageFieldSerializer(required=False, allow_null=True, sizes='product_size')

    name = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = '__all__'

    def get_name(self, obj):
        return obj.image.name

class HomeContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeContent
        fields = '__all__'