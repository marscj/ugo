from rest_framework import  serializers
from rest_framework.validators import UniqueValidator
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Category, Product, ProductVariant, ProductImage, VariantImage

class CategorySerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True, null=False, max_length=16, validators=[UniqueValidator(queryset=Category.objects.all())])

    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True, null=False, max_length=128, validators=[UniqueValidator(queryset=Product.objects.all())])

    image = VersatileImageFieldSerializer(required=True, null=False, many=False)

    category = CategorySerializer(required=True, null=False, many=False)

    class Meta:
        model = Product
        fields = '__all__'

class ProductVariantSerializer(serializers.ModelSerializer):

    sku = serializers.CharField(required=True, null=False, max_length=32, validators=[UniqueValidator(queryset=ProductVariant.objects.all())])

    name = serializers.CharField(required=True, null=False, max_length=128, validators=[UniqueValidator(queryset=Product.objects.all())])

    product = ProductSerializer(required=True, null=False, many=False)

    images = ProductImageSerializer(required=False, null=True, many=True)

    class Meta:
        model = ProductVariant
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):

    product = ProductSerializer(required=False, null=True, many=False)

    image = VersatileImageFieldSerializer(required=True, null=False, many=False)

    class Meta:
        model = ProductImage
        fields = '__all__'

