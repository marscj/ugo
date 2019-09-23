from django.db.models import Min, Max, Avg, Q
from rest_framework import  serializers

from .models import Coupon
from app.authorization.models import CustomUser
from app.product.serializers import VariantSerializer
from app.authorization.serializers import UserSimpleSerializer

class CouponSerializer(serializers.ModelSerializer):

    couponID = serializers.ReadOnlyField()

    enable = serializers.BooleanField(default=True)

    amount = serializers.DecimalField(default=0.0, max_digits=10, decimal_places=2, min_value=0.0)

    exp_date = serializers.DateField()

    description = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=128)

    variant = VariantSerializer(read_only=True, many=False)

    customer = UserSimpleSerializer(read_only=True, many=True)

    variant_id = serializers.IntegerField()

    customer_id = serializers.PrimaryKeyRelatedField(required=False, allow_null=True, write_only=True, many=True, queryset=CustomUser.objects.all())

    class Meta:
        model = Coupon
        fields = (
           'id', 'couponID', 'enable', 'amount', 'exp_date', 'description', 'variant_id', 'customer_id', 'variant', 'customer'
        )

    def create(self, validated_data):
        customer = validated_data.pop('customer_id', None)
        coupon = Coupon.objects.create(**validated_data)
        
        if customer is not None:
            for data in customer:
                coupon.customer.add(data)
    
        return coupon

    def update(self, instance, validated_data):
        customer = validated_data.pop('customer_id', None)

        if customer is not None:
            for data in instance.customer.all():
                instance.customer.remove(data)

            for data in customer:
                instance.customer.add(data)

        super().update(instance, validated_data)

        return instance
