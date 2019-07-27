from rest_framework import  serializers
from rest_framework.validators import UniqueValidator

from .models import Order
from app.authorization.models import CustomUser
from app.product.models import ProductVariant
from app.product.serializers import ProductVariantSerializer
from app.authorization.serializers import UserSimpleSerializer, UserSerializer

class OrderSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    orderID = serializers.CharField(read_only=True)

    confirmID = serializers.CharField(required=False, allow_null=True, max_length=64)

    order_status = serializers.IntegerField(required=False)

    day = serializers.DateField()

    time = serializers.TimeField()

    customer_info = serializers.CharField(required=False)

    customer_contact = serializers.CharField(required=False)

    adult_quantity = serializers.IntegerField(required=False, allow_null=True, min_value=0, max_value=9999)

    adult_price = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2, min_value=0.0)

    child_quantity = serializers.IntegerField(required=False, allow_null=True, min_value=0, max_value=9999)

    child_price = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2, min_value=0.0)

    remark = serializers.CharField(required=False, allow_null=True)

    variant = serializers.StringRelatedField(read_only=True)

    customer = serializers.StringRelatedField(read_only=True)

    operator = serializers.StringRelatedField(read_only=True)

    variant_id = serializers.IntegerField()

    customer_id = serializers.IntegerField()

    operator_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Order
        fields = '__all__'

    def validate(self, data):
        adult_quantity = data.get('adult_quantity')
        child_quantity = data.get('child_quantity')

        customer_id = data.get('customer_id')
        variant_id = data.get('variant_id')
        operator_id = data.get('operator_id')

        if adult_quantity is None and child_quantity is None:
            raise serializers.ValidationError({'adult_quantity': 'adult quantity or child quantity is requried.', 'child_quantity': 'adult quantity or child quantity requried'})
        elif adult_quantity == 0 and child_quantity == 0:
            raise serializers.ValidationError({'adult_quantity': 'adult quantity or child quantity is a minimum of 1.', 'child_quantity': 'adult quantity or child quantity is a minimum of 1'})

        try:
            ProductVariant.objects.get(pk=variant_id)
        except ProductVariant.DoesNotExist:
            raise serializers.ValidationError({'variant': 'not found.'})

        try:
            CustomUser.objects.get(pk=customer_id)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError({'customer': 'not found.'})

        if operator_id is not None:
            try:
                CustomUser.objects.get(pk=operator_id)
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError({'operator': 'not found.'})

        return super().validate(data)

    def create(self, validated_data):
        adult_quantity = validated_data.get('adult_quantity')
        child_quantity = validated_data.get('child_quantity')
        variant_id = validated_data.get('variant_id')
        customer_id = validated_data.get('customer_id')

        variant = ProductVariant.objects.get(pk=variant_id)
        customer = CustomUser.objects.get(pk=customer_id)

        adult_price = adult_quantity * variant.adult_price[customer.price_level - 1]
        child_price = child_quantity * variant.child_price[customer.price_level - 1]

        return Order.objects.create(**validated_data, adult_price=adult_price, child_price=child_price)

    def update(self, instance, validated_data):
        adult_quantity = validated_data.get('adult_quantity')
        child_quantity = validated_data.get('child_quantity')
        variant_id = validated_data.get('variant_id')
        customer_id = validated_data.get('customer_id')

        variant = ProductVariant.objects.get(pk=variant_id)
        customer = CustomUser.objects.get(pk=customer_id)

        instance.adult_price = adult_quantity * variant.adult_price[customer.price_level - 1]
        instance.child_price = child_quantity * variant.child_price[customer.price_level - 1]
        
        return super().update(instance, validated_data)