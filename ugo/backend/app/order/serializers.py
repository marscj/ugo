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

    pay_status = serializers.IntegerField(required=False)

    day = serializers.DateField()

    time = serializers.TimeField()

    customer_info = serializers.CharField(required=False, allow_null=True)

    customer_contact = serializers.CharField(required=False, allow_null=True)

    adult_quantity = serializers.IntegerField(min_value=0, max_value=9999)

    adult_price = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2, min_value=0.0)

    child_quantity = serializers.IntegerField(min_value=0, max_value=9999)

    child_price = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2, min_value=0.0)

    remark = serializers.CharField(required=False, allow_null=True)

    variant = serializers.StringRelatedField(read_only=True)

    customer = serializers.StringRelatedField(read_only=True)

    operator = serializers.StringRelatedField(read_only=True)

    variant_id = serializers.IntegerField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_info(self, validated_data):
        adult_quantity = validated_data.get('adult_quantity', 0)
        child_quantity = validated_data.get('child_quantity', 0)
        variant_id = validated_data.get('variant_id')

        variant = ProductVariant.objects.get(pk=variant_id)
        customer = self.context['request'].user

        return {
            'adult_price': adult_quantity * variant.adult_price[customer.price_level - 1],
            'child_price': child_quantity * variant.child_price[customer.price_level - 1],
            'variant': variant,
        }

    def validate(self, data):
        adult_quantity = data.get('adult_quantity', 0)
        child_quantity = data.get('child_quantity', 0)
        variant_id = data.get('variant_id')
        customer = self.context['request'].user

        if adult_quantity == 0 and child_quantity == 0:
            raise serializers.ValidationError({'adult_quantity': '成人数量或者儿童数量至少为1', 'child_quantity': '成人数量或者儿童数量至少为1'})
        
        try:
            variant = ProductVariant.objects.get(pk=variant_id)
            if not variant.status or not variant.product.status:
                raise serializers.ValidationError({'variant': '此产品已下架'})
        except ProductVariant.DoesNotExist:
            raise serializers.ValidationError({'variant': '产品不存在'})

        info = self.get_info(data)
        adult_price = info['adult_price']
        child_price = info['child_price']
        
        if customer.balance < adult_price + child_price:
            raise serializers.ValidationError({'customer': '账户余额不足'})

        return super().validate(data)

    def create(self, validated_data):
        info = self.get_info(validated_data)
        adult_price = info['adult_price']
        child_price = info['child_price']
        customer = self.context['request'].user

        customer.balance -= adult_price + child_price
        customer.save()

        return Order.objects.create(**validated_data, adult_price=adult_price, child_price=child_price, customer=customer)

    def update(self, instance, validated_data):
        if instance.operator is None:
            instance.operator = self.context['request'].user
        return super().update(instance, validated_data)