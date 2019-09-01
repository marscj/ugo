from django.db.models import Min, Max, Avg, Q
from rest_framework import  serializers
from rest_framework.validators import UniqueValidator

from .models import Category, Product, ProductVariant
from app.source.models import ProductImage
from app.source.serializers import ProductImageSerializer
from app.authorization.models import CustomUser

class VariantSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()

    status = serializers.BooleanField()

    variantID = serializers.CharField(allow_null=False, max_length=16, validators=[UniqueValidator(queryset=ProductVariant.objects.all())])
 
    name = serializers.CharField(allow_null=False, max_length=64)

    sku = serializers.CharField(allow_null=False, max_length=32, validators=[UniqueValidator(queryset=ProductVariant.objects.all())])

    adult_status = serializers.BooleanField()

    adult_desc = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=64)

    adult_quantity = serializers.HiddenField(default=0)

    adult_price = serializers.ListField(required=False, allow_null=True, allow_empty=False, min_length=5, max_length=5, child=serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.0))

    child_status = serializers.BooleanField()

    child_desc = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=64)

    child_quantity = serializers.HiddenField(default=0)

    child_price = serializers.ListField(required=False, allow_null=True, allow_empty=False, min_length=5, max_length=5, child=serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.0))

    product = serializers.StringRelatedField(read_only=True)

    product_id = serializers.IntegerField(required=True)

    category = serializers.SerializerMethodField()

    sort_by = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = ProductVariant
        fields = '__all__'

    def get_category(self, obj):
        return obj.product.category

    def validate(self, data):
        adult_status = data.get('adult_status', False)
        adult_price = data.get('adult_price')

        child_status = data.get('child_status', False)
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

class ProductVariantSerializer(serializers.ModelSerializer):

    status = serializers.ReadOnlyField()

    variantID = serializers.ReadOnlyField()
 
    name = serializers.ReadOnlyField()

    sku = serializers.ReadOnlyField()

    adult_status = serializers.ReadOnlyField()

    adult_desc = serializers.ReadOnlyField()

    adult_quantity = serializers.HiddenField(default=0)

    child_status = serializers.ReadOnlyField()

    child_desc = serializers.ReadOnlyField()

    child_quantity = serializers.HiddenField(default=0)

    sort_by = serializers.ReadOnlyField()

    adult_price = serializers.SerializerMethodField()

    child_price = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariant
        fields = '__all__'

    def get_user(self):
        return self.context['request'].user

    def get_price_lelve(self):
        if isinstance(self.get_user(), CustomUser):
            return self.get_user().price_level - 1
        else:
            return 4

    def get_adult_price(self, obj):
        return obj.adult_price[self.get_price_lelve()]

    def get_child_price(self, obj):
        return obj.child_price[self.get_price_lelve()]


class ProductListSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()

    status = serializers.ReadOnlyField()

    category = serializers.ReadOnlyField()

    productID = serializers.ReadOnlyField()

    title = serializers.ReadOnlyField()

    subtitle = serializers.ReadOnlyField()

    location = serializers.ReadOnlyField()

    photo = ProductImageSerializer(read_only=True)

    sort_by = serializers.HiddenField(default=0)

    class Meta:
        model = Product
        fields = (
            'id', 'status', 'category', 'productID', 'title', 'subtitle', 'location', 'photo', 'sort_by'
        )

class ProductSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()

    status = serializers.BooleanField()

    category = serializers.IntegerField()

    productID = serializers.CharField(allow_null=False, max_length=16, validators=[UniqueValidator(queryset=Product.objects.all())])

    title = serializers.CharField(allow_null=False, max_length=128, validators=[UniqueValidator(queryset=Product.objects.all())])

    subtitle = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=2048)

    special = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=512)

    location = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=32)

    content = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    photo_id = serializers.IntegerField(required=False, allow_null=True, write_only=True)

    gallery_id = serializers.PrimaryKeyRelatedField(required=False, allow_null=True, write_only=True, many=True, queryset=ProductImage.objects.all())

    photo = ProductImageSerializer(read_only=True)

    gallery = ProductImageSerializer(read_only=True, many=True)
    
    variant = serializers.SerializerMethodField()

    sort_by = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_variant(self, obj):
        variant_queryset = ProductVariant.objects.all().filter(status=True).filter(product=obj.id).order_by('sort_by')
        serializer = ProductVariantSerializer(instance=variant_queryset, many=True, context=self.context)
        return serializer.data

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

        if gallery is not None:
            for data in instance.gallery.all():
                instance.gallery.remove(data)

            for data in gallery:
                instance.gallery.add(data)

        if photo is not None:
            instance.photo_id = photo

        super().update(instance, validated_data)

        return instance