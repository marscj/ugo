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

    name = serializers.CharField(required=True, allow_null=False, max_length=128, validators=[UniqueValidator(queryset=Product.objects.all())])

    category = CategorySerializer(required=False, allow_null=False, many=False)

    image = ProductImageSerializer(many=True)

    icon = serializers.SerializerMethodField()

    gallery = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'productID', 'name', 'category', 'image', 'icon', 'gallery')
    
    def get_icon(self, obj):
        icon = obj.image.filter(flag='icon').last()
        # print(icon.image.thumbnail['400x400'].url)
        if icon is not None:
            return icon.image.thumbnail['400x400'].url
        return None

    def get_gallery(self, obj):
        return None
        # return obj.image.filter(flag='gallery')

class ProductVariantSerializer(serializers.ModelSerializer):

    productID = serializers.CharField(required=True, allow_null=False, max_length=16, validators=[UniqueValidator(queryset=ProductVariant.objects.all())])

    sku = serializers.CharField(required=True, allow_null=False, max_length=32, validators=[UniqueValidator(queryset=ProductVariant.objects.all())])

    name = serializers.CharField(required=True, allow_null=False, max_length=128, validators=[UniqueValidator(queryset=Product.objects.all())])

    product = ProductSerializer(required=True, allow_null=False, many=False)
 
    class Meta:
        model = ProductVariant
        fields = '__all__'

