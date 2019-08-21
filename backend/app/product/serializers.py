from django.db.models import Min, Max, Avg
from rest_framework import  serializers
from rest_framework.validators import UniqueValidator

from .models import Category, Product, ProductVariant
from app.source.models import ProductImage
from app.source.serializers import ProductImageSerializer
from app.authorization.models import CustomUser

class ProductVariantSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()

    status = serializers.ReadOnlyField()

    variantID = serializers.ReadOnlyField()

    name = serializers.ReadOnlyField()

    sku = serializers.ReadOnlyField()

    adult_status = serializers.ReadOnlyField()

    adult_desc = serializers.ReadOnlyField()

    adult_quantity = serializers.ReadOnlyField()

    adult_price = serializers.SerializerMethodField('user_adult_price')

    child_status = serializers.ReadOnlyField()

    child_desc = serializers.ReadOnlyField()

    child_quantity = serializers.ReadOnlyField()

    child_price = serializers.SerializerMethodField('user_child_price')

    product = serializers.StringRelatedField(read_only=True)

    category = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariant
        # fields = '__all__'
        exclude = ['is_delete']

    def get_user_price_lelve(self):
        if isinstance(self.context['request'].user, CustomUser):
            return self.context['request'].user.price_level - 1
        else:
            return 4

    def user_adult_price(self, obj):
        return obj.adult_price[self.get_user_price_lelve()]

    def user_child_price(self, obj):
        return obj.child_price[self.get_user_price_lelve()]

    def get_category(self, obj):
        return obj.product.category

class ProductVariantBackendSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()

    status = serializers.BooleanField()

    variantID = serializers.CharField(allow_null=False, max_length=16, validators=[UniqueValidator(queryset=ProductVariant.objects.all())])
 
    name = serializers.CharField(allow_null=False, max_length=64)

    sku = serializers.CharField(allow_null=False, max_length=32, validators=[UniqueValidator(queryset=ProductVariant.objects.all())])

    adult_status = serializers.BooleanField()

    adult_desc = serializers.CharField(required=False, allow_null=True, max_length=64)

    adult_quantity = serializers.IntegerField(required=False, allow_null=True, min_value=0, max_value=9999)

    adult_price = serializers.ListField(required=False, allow_null=True, allow_empty=False, min_length=5, max_length=5, child=serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.0))

    child_status = serializers.BooleanField()

    child_desc = serializers.CharField(required=False, allow_null=True, max_length=64)

    child_quantity = serializers.IntegerField(required=False, allow_null=True, min_value=0, max_value=9999)

    child_price = serializers.ListField(required=False, allow_null=True, allow_empty=False, min_length=5, max_length=5, child=serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.0))

    product = serializers.StringRelatedField(read_only=True)

    product_id = serializers.IntegerField(required=True)

    category = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariant
        exclude = ['is_delete']

    def get_category(self, obj):
        return obj.product.category

    def validate(self, data):
        adult_status = data.get('adult_status', False)
        adult_quantity = data.get('adult_quantity')
        adult_price = data.get('adult_price')

        child_status = data.get('child_status', False)
        child_quantity = data.get('child_quantity')
        child_price = data.get('child_price')

        product_id = data.get('product_id')
    
        if adult_status:
            if adult_price is None:
                raise serializers.ValidationError({'adult_price': 'adult price is required.'})

        if child_status:
            if child_price is None:
                raise serializers.ValidationError({'child_price': 'child price is required.'})

        try:
            Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError({'product_id': 'Not Found.'})

        return super().validate(data)

class ProductListSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()

    status = serializers.ReadOnlyField()

    category = serializers.ReadOnlyField()

    productID = serializers.ReadOnlyField()

    title = serializers.ReadOnlyField()

    subtitle = serializers.ReadOnlyField()

    location = serializers.ReadOnlyField()

    photo = ProductImageSerializer(read_only=True)

    sort_by = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = (
            'id', 'status', 'category', 'productID', 'title', 'subtitle', 'location', 'photo', 'sort_by'
        )

class ProductSerializer(ProductListSerializer):

    location = serializers.ReadOnlyField()

    special = serializers.ReadOnlyField()

    content = serializers.ReadOnlyField()

    gallery = ProductImageSerializer(read_only=True, many=True)

    variant = ProductVariantSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        exclude = ['is_delete']

class ProductBackendSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()

    status = serializers.BooleanField()

    category = serializers.IntegerField()

    productID = serializers.CharField(allow_null=False, max_length=16, validators=[UniqueValidator(queryset=Product.objects.all())])

    title = serializers.CharField(allow_null=False, max_length=128, validators=[UniqueValidator(queryset=Product.objects.all())])

    subtitle = serializers.CharField(required=False, allow_null=True, max_length=2048)

    special = serializers.CharField(required=False, allow_null=True, max_length=512)

    location = serializers.CharField(required=False, allow_null=True, max_length=32)

    content = serializers.CharField(required=False, allow_null=True)

    photo_id = serializers.IntegerField(required=False, allow_null=True, write_only=True)

    gallery_id = serializers.PrimaryKeyRelatedField(required=False, allow_null=True, write_only=True, many=True, queryset=ProductImage.objects.all())

    photo = ProductImageSerializer(read_only=True)

    gallery = ProductImageSerializer(read_only=True, many=True)

    variant = ProductVariantSerializer(read_only=True, many=True)

    sort_by = serializers.CharField(required=False, allow_null=True, max_length=32)

    class Meta:
        model = Product
        exclude = ['is_delete']

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