from rest_framework import  serializers
from rest_framework.validators import UniqueValidator

from .models import Category, Product, ProductVariant
from app.source.serializers import ProductImageSerializer

class CategorySerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True, allow_null=False, max_length=16, validators=[UniqueValidator(queryset=Category.objects.all())])

    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    productID = serializers.CharField(required=True, allow_null=False, max_length=16, validators=[UniqueValidator(queryset=Product.objects.all())])

    title = serializers.CharField(required=True, allow_null=False, max_length=128)

    subtitle = serializers.CharField(required=True, allow_null=False, max_length=512)

    location = serializers.CharField(required=True, allow_null=False, max_length=32)

    content = serializers.CharField(required=False, allow_null=True, max_length=2048)

    category = CategorySerializer(required=True, allow_null=False, many=False)

    photo = ProductImageSerializer(required=True, many=False)

    gallery = ProductImageSerializer(required=False, many=True)

    class Meta:
        model = Product
        fields = '__all__'

class ProductVariantSerializer(serializers.ModelSerializer):

    productID = serializers.CharField(required=True, allow_null=False, max_length=16, validators=[UniqueValidator(queryset=ProductVariant.objects.all())])

    sku = serializers.CharField(required=True, allow_null=False, max_length=32, validators=[UniqueValidator(queryset=ProductVariant.objects.all())])

    name = serializers.CharField(required=True, allow_null=False, max_length=128, validators=[UniqueValidator(queryset=Product.objects.all())])

    product = ProductSerializer(required=True, allow_null=False, many=False)
 
    class Meta:
        model = ProductVariant
        fields = '__all__'

