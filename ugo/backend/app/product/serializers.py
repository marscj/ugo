from rest_framework import  serializers
from rest_framework.validators import UniqueValidator

from .models import Category, Product, ProductVariant
from app.source.models import ProductImage
from app.source.serializers import ProductImageSerializer

class CategorySerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True, allow_null=False, max_length=16, validators=[UniqueValidator(queryset=Category.objects.all())])

    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    productID = serializers.CharField(allow_null=False, max_length=16, validators=[UniqueValidator(queryset=Product.objects.all())])

    title = serializers.CharField(allow_null=False, max_length=128, validators=[UniqueValidator(queryset=Product.objects.all())])

    subtitle = serializers.CharField(allow_null=False, max_length=512)

    location = serializers.CharField(allow_null=False, max_length=32)

    content = serializers.CharField(allow_null=True, max_length=2048)

    category = CategorySerializer(read_only=True)

    category_id = serializers.IntegerField(write_only=True)

    photo = ProductImageSerializer(read_only=True)

    photo_id = serializers.IntegerField(write_only=True)

    gallery = ProductImageSerializer(read_only=True, many=True)

    gallery_id = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=ProductImage.objects.all())

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        gallery = validated_data.pop('gallery_id', None)
        photo = validated_data.pop('photo_id', None)
        product = Product.objects.create(**validated_data, photo_id=photo)
        
        if gallery is not None:
            for data in gallery:
                product.gallery.add(data)

        return product

    def update(self, instance, validated_data):
        gallery = validated_data.pop('gallery_id', None)
        photo = validated_data.pop('photo_id', None)

        for data in instance.gallery.all():
            instance.gallery.remove(data)

        if gallery is not None:
            for data in gallery:
                instance.gallery.add(data)

        instance.photo_id = photo

        super().update(instance, validated_data)
        print('==============')
        print(instance.subtitle)
        print('==============')

        return instance

class ProductVariantSerializer(serializers.ModelSerializer):

    productID = serializers.CharField(required=True, allow_null=False, max_length=16, validators=[UniqueValidator(queryset=ProductVariant.objects.all())])

    sku = serializers.CharField(required=True, allow_null=False, max_length=32, validators=[UniqueValidator(queryset=ProductVariant.objects.all())])

    name = serializers.CharField(required=True, allow_null=False, max_length=128, validators=[UniqueValidator(queryset=Product.objects.all())])

    product = ProductSerializer(required=True, allow_null=False, many=False)
 
    class Meta:
        model = ProductVariant
        fields = '__all__'
