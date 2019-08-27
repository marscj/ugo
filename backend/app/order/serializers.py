from rest_framework import  serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import AnonymousUser
from django.db import transaction

from decimal import Decimal

from .models import Order
from app.authorization.models import CustomUser
from app.product.models import ProductVariant, Product
from app.product.serializers import ProductVariantSerializer
from app.authorization.serializers import UserSimpleSerializer, UserSerializer

class CheckoutSerializer(serializers.Serializer):

    day = serializers.DateField()

    time = serializers.TimeField()

    adult_quantity = serializers.IntegerField(default=0, min_value=0, max_value=9999)

    child_quantity = serializers.IntegerField(default=0, min_value=0, max_value=9999)

    productID = serializers.IntegerField()

    variantID = serializers.IntegerField()

    adult_price = serializers.SerializerMethodField()

    child_price = serializers.SerializerMethodField()

    def get_user(self):
        return self.context['request'].user

    def get_balance(self):
        return self.get_user().balance

    def get_price_lelve(self):
        if isinstance(self.get_user(), CustomUser):
            return self.get_user().price_level - 1
        else:
            return 4

    def get_adult_price(self, obj):
        variant = self.get_variant(obj['variantID'])
        return variant.adult_price[self.get_price_lelve()] * obj['adult_quantity']

    def get_child_price(self, obj):
        variant = self.get_variant(obj['variantID'])
        return variant.child_price[self.get_price_lelve()] * obj['child_quantity']

    def get_variant(self, value):
        return ProductVariant.objects.get(variantID=value)

    def get_product(self, value):
        return Product.objects.get(productID=value)

    def validate_day(self, value):
        return value
    
    def validate_time(self, value):
        return value
 
    def validate_adult_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError('成人数量或者儿童数量至少为1')
        return value
    
    def validate_child_quantity(self, value):
        return value
    
    def validate_productID(self, value):
        try:
            product = Product.objects.get(productID=value)
            if not product.status:
                raise serializers.ValidationError('此产品已下架')
            return value
        except Product.DoesNotExist:
            raise serializers.ValidationError('产品不存在')

    def validate_variantID(self, value):
        try:
            variant = ProductVariant.objects.get(variantID=value)
            if not variant.status:
                raise serializers.ValidationError('此产品已下架')
            return value
        except ProductVariant.DoesNotExist:
            raise serializers.ValidationError('产品不存在')

    def validate(self, validate_data):
        balance = self.get_balance()
        adult_price = self.get_adult_price(validate_data)
        child_price = self.get_child_price(validate_data)

        if balance < adult_price + child_price:
            raise serializers.ValidationError({'customer': '账户余额不足'})

        return validate_data

class OrderCreateSerializer(CheckoutSerializer):

    id = serializers.ReadOnlyField()

    orderID = serializers.ReadOnlyField()

    confirmID = serializers.ReadOnlyField()

    order_status = serializers.ReadOnlyField()

    pay_status = serializers.ReadOnlyField()

    create_at = serializers.ReadOnlyField()

    change_at = serializers.ReadOnlyField()

    adult_price = serializers.ReadOnlyField()

    child_price = serializers.ReadOnlyField()

    total = serializers.ReadOnlyField()

    remark = serializers.ReadOnlyField()

    product = serializers.ReadOnlyField()

    variant = serializers.ReadOnlyField()

    category = serializers.ReadOnlyField()

    sku = serializers.ReadOnlyField()

    customer = serializers.ReadOnlyField()

    customer_id = serializers.ReadOnlyField()

    operator = serializers.ReadOnlyField()

    operator_id = serializers.ReadOnlyField()

    is_delete = serializers.ReadOnlyField()

    guest_info = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    guest_contact = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    guest_remark = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    order_from = serializers.CharField(default='ugodubai')

    class Meta:
        model = Order 
        fields = '__all__'

    def get_total(self, validated_data):
        return Decimal(self.get_adult_price(validate_data)) + Decimal(self.get_child_price(validate_data))

    def payment(self, total):
        customer = self.get_user()
        customer.balance -= total
        customer.save()

    @transaction.atomic
    def create(self, validated_data):
        adult_price = self.get_adult_price(validate_data)
        child_price = self.get_child_price(validate_data)
        total = self.get_total(validated_data)
        product = self.get_product(validated_data).title
        variant = self.get_variant(validated_data).name
        category = product.category
        sku = variant.sku
        customer=self.get_user().username
        customer_id=self.get_user().id

        self.payment(total)

        return Order.objects.create(**validated_data,
            adult_price=adult_price,
            child_price=child_price,
            total=total,
            product=product
            variant=variant
            category=category
            sku=sku
            customer=customer
            customer_id=customer_id
        )

    @transaction.atomic
    def update(self, instance, validated_data):
        if instance.operator is None:
            instance.operator = self.context['request'].user
        return super().update(instance, validated_data)

class OrderUpdateSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()

    orderID = serializers.ReadOnlyField()

    day = serializers.ReadOnlyField()

    time = serializers.ReadOnlyField()

    adult_quantity = serializers.ReadOnlyField()

    child_quantity = serializers.ReadOnlyField()

    adult_price = serializers.ReadOnlyField()

    child_price = serializers.ReadOnlyField()

    total = serializers.ReadOnlyField()

    variant_id = serializers.ReadOnlyField()

    confirmID = serializers.CharField(required=False, allow_null=True, max_length=64)

    order_status = serializers.IntegerField(required=False)

    pay_status = serializers.IntegerField(required=False)

    guest_info = serializers.CharField(required=False, allow_null=True)

    customer_contact = serializers.CharField(required=False, allow_null=True)

    guest_remark = serializers.CharField(required=False, allow_null=True)

    variant = serializers.StringRelatedField(read_only=True)

    customer = serializers.StringRelatedField(read_only=True)

    operator = serializers.StringRelatedField(read_only=True)

    product = serializers.SerializerMethodField()

    class Meta:
        model = Order 
        fields = '__all__'

    def get_product(self, obj):
        if obj.variant:
            return obj.variant.product.title
            
    @transaction.atomic
    def update(self, instance, validated_data):
        if instance.operator is None:
            instance.operator = self.context['request'].user
        return super().update(instance, validated_data)