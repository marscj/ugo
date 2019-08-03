from rest_framework import  serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import AnonymousUser
from django.db import transaction

from decimal import Decimal

from .models import Order
from app.authorization.models import CustomUser
from app.product.models import ProductVariant
from app.product.serializers import ProductVariantSerializer
from app.authorization.serializers import UserSimpleSerializer, UserSerializer

class CheckoutOrderSerializer(serializers.ModelSerializer):
    
    day = serializers.DateField()

    time = serializers.TimeField()

    adult_quantity = serializers.IntegerField(min_value=0, max_value=9999)

    child_quantity = serializers.IntegerField(min_value=0, max_value=9999)

    adult_price = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.0)

    child_price = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.0)

    total_price = serializers.ReadOnlyField()

    variant_id = serializers.IntegerField()

    class Meta:
        model = Order 
        fields = '__all__'

    def get_current_user(self):
        return self.context['request'].user

    def get_user_price_lelve(self):
        if isinstance(self.context['request'].user, CustomUser):
            return self.context['request'].user.price_level - 1
        else:
            return 4
        
    def _get_adult_price(self, variant, quantity):
        return quantity * variant.adult_price[self.get_user_price_lelve()]

    def _get_child_price(self, variant, quantity):
        return quantity * variant.child_price[self.get_user_price_lelve()]

    def _get_total_price(self, validated_data):
        if self.variant is not None:
            adult_price = self._get_adult_price(self.variant, validated_data.get('adult_quantity', 0.0))
            child_price = self._get_child_price(self.variant, validated_data.get('child_quantity', 0.0))
            return Decimal(adult_price) + Decimal(child_price)

    def _get_variant(self, variant_id):
        try:
            self.variant = ProductVariant.objects.get(pk=variant_id)
            if not self.variant.status or not self.variant.product.status:
                raise serializers.ValidationError({'variant': '此产品已下架'})
            return self.variant
        except ProductVariant.DoesNotExist:
            raise serializers.ValidationError({'variant': '产品不存在'})

    def validate_quantity(self, adult_quantity, child_quantity):
        if adult_quantity == 0 and child_quantity == 0:
            raise serializers.ValidationError({'adult_quantity': '成人数量或者儿童数量至少为1', 'child_quantity': '成人数量或者儿童数量至少为1'})

    def validate_price(self, adult_price, child_price, _adult_price, _child_price):
        if adult_price != _adult_price:
            raise serializers.ValidationError({'adult_price': '价格已发生变化'})

        if child_price != _child_price:
            raise serializers.ValidationError({'adult_price': '价格已发生变化'})

    def validate_balance(self, adult_price, child_price):
        customer = self.get_current_user()

        if isinstance(customer, CustomUser):
            if customer.balance < adult_price + child_price: 
                raise serializers.ValidationError({'customer': '账户余额不足'})

    def validate_customer(self):
        customer = self.get_current_user()

        if isinstance(customer, AnonymousUser):
            raise serializers.ValidationError({'customer': '请登陆用户'})

    def validate(self, data):
        adult_quantity = data.get('adult_quantity', 0)
        child_quantity = data.get('child_quantity', 0)
        adult_price = data.get('adult_price', 0.0)
        child_price = data.get('child_price', 0.0)
        variant_id = data.get('variant_id')

        self.validate_customer()
        self.validate_quantity(adult_quantity, child_quantity)

        variant = self._get_variant(variant_id)
        _adult_price = self._get_adult_price(variant, adult_quantity)
        _child_price = self._get_child_price(variant, child_quantity)

        self.validate_balance(_adult_price, _child_price)
        self.validate_price(adult_price, child_price, _adult_price, _child_price)

        return super().validate(data)

class OrderSerializer(CheckoutOrderSerializer):

    id = serializers.IntegerField(read_only=True)

    orderID = serializers.CharField(read_only=True)

    confirmID = serializers.CharField(required=False, allow_null=True, max_length=64)

    order_status = serializers.IntegerField(required=False)

    pay_status = serializers.IntegerField(required=False)

    customer_info = serializers.CharField(required=False, allow_null=True)

    customer_contact = serializers.CharField(required=False, allow_null=True)

    remark = serializers.CharField(required=False, allow_null=True)

    variant = serializers.StringRelatedField(read_only=True)

    customer = serializers.StringRelatedField(read_only=True)

    operator = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order 
        fields = '__all__'

    @transaction.atomic
    def create(self, validated_data):
        # validated_data.pop('total_price')
        customer = self.get_current_user()
        total_price = self._get_total_price(validated_data)

        customer.balance -= total_price
        customer.save()
 
        return Order.objects.create(**validated_data, total_price=total_price, customer=customer)

    @transaction.atomic
    def update(self, instance, validated_data):
        if instance.operator is None:
            instance.operator = self.context['request'].user
        return super().update(instance, validated_data)