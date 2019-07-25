from rest_framework import  serializers
from rest_framework.validators import UniqueValidator

from .models import Category, Product, ProductVariant
from app.source.models import ProductImage
from app.source.serializers import ProductImageSerializer

class ProductSerializer(serializers.ModelSerializer):

    status = serializers.BooleanField(required=True)

    productID = serializers.CharField(required=True, allow_null=False, max_length=16, validators=[UniqueValidator(queryset=Product.objects.all())])

    name = serializers.CharField(required=True, allow_null=False, max_length=128, validators=[UniqueValidator(queryset=Product.objects.all())])

    description = serializers.CharField(required=True, allow_null=False, max_length=128)

    subtitle = serializers.CharField(required=True, allow_null=False, max_length=512)

    location = serializers.CharField(required=True, allow_null=False, max_length=32)

    content = serializers.CharField(required=True, allow_null=True)

    photo = ProductImageSerializer(read_only=True)

    photo_id = serializers.IntegerField(required=True, write_only=True)

    gallery = ProductImageSerializer(read_only=True, many=True)

    gallery_id = serializers.PrimaryKeyRelatedField(required=True, write_only=True, many=True, queryset=ProductImage.objects.all())

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

        return instance

class ProductVariantSerializer(serializers.ModelSerializer):

    status = serializers.BooleanField(required=True)

    variantID = serializers.CharField(required=True, allow_null=False, max_length=16, validators=[UniqueValidator(queryset=ProductVariant.objects.all())])

    name = serializers.CharField(required=True, allow_null=False, max_length=64, validators=[UniqueValidator(queryset=Product.objects.all())])

    sku = serializers.CharField(required=True, allow_null=False, max_length=32, validators=[UniqueValidator(queryset=ProductVariant.objects.all())])

    adult_status = serializers.BooleanField(required=True)

    adult_desc = serializers.CharField(required=False, allow_null=True, max_length=64)

    adult_quantity = serializers.IntegerField(required=False, allow_null=True, min_value=0, max_value=9999)

    adult_price = serializers.ListField(required=False, allow_null=True)

    child_status = serializers.BooleanField(required=True)

    child_desc = serializers.CharField(required=False, allow_null=True, max_length=64)

    child_quantity = serializers.IntegerField(required=False, allow_null=True, min_value=0, max_value=9999)

    child_price = serializers.ListField(required=False, allow_null=True)

    product = ProductSerializer(read_only=True)

    product_id = serializers.IntegerField(required=True)

    class Meta:
        model = ProductVariant
        fields = '__all__'

    def validate(self, data):
        adult_status = data.get('adult_status', False)
        adult_quantity = data.get('adult_quantity')
        adult_price = data.get('adult_price')

        child_status = data.get('child_status', False)
        child_quantity = data.get('child_quantity')
        child_price = data.get('child_price')
    
        if adult_status:
            # if adult_quantity is None:
            #     raise serializers.ValidationError({'adult_quantity': 'adult quantity is required.'})

            if adult_price is None:
                raise serializers.ValidationError({'adult_price': 'adult price is required.'})

        if child_status:
            # if child_quantity is None:
            #     raise serializers.ValidationError({'child_quantity': 'child quantity is required.'})

            if child_price is None:
                raise serializers.ValidationError({'child_price': 'child price is required.'})

        return data
    

