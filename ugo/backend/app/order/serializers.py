from rest_framework import  serializers
from rest_framework.validators import UniqueValidator

from .models import Order
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

    contact = serializers.CharField(required=False)

    phone = serializers.CharField(required=False)

    adult_quantity = serializers.IntegerField(required=False, allow_null=True, min_value=0, max_value=9999)

    adult_price = models.DecimalField(read_only=True)

    child_quantity = serializers.IntegerField(required=False, allow_null=True, min_value=0, max_value=9999)

    child_price = models.DecimalField(read_only=True)

    remark = models.TextField(required=False, allow_null=True)

    variant = ProductVariantSerializer(read_only=True)

    variant_id = serializers.IntegerField()

    customer = UserSerializer(read_only=True)

    customer_id = serializers.IntegerField()

    operator = UserSimpleSerializer(read_only=True)

    operator_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Order
        fields = '__all__'

    def validate(self, data):
        adult_quantity = data.get('adult_quantity')
        adult_price = data.get('adult_price')

        child_quantity = data.get('child_quantity')
        child_price = data.get('child_price')

        if adult_quantity is None and child_quantity is None:
            raise serializers.ValidationError({'adult_quantity': 'adult quantity or child quantity is a minimum of 1.', 'child_quantity': 'adult quantity or child quantity is a minimum of 1'})

        return data

    def create(self, validated_data):

        adult_price = self.adult_quantity * self.variant.adult_price[self.customer.price_level]

        child_price = self.child_quantity * self.variant.child_price[self.customer.price_level]

        return Order.objects.create(**validated_data, adult_price=adult_price, child_price=child_price)

    