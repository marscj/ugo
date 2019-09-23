from rest_framework import  serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import AnonymousUser
from django.db import transaction

from decimal import Decimal

from .import OrderStatus
from .models import Order
from app.authorization.models import CustomUser
from app.product.models import ProductVariant, Product
from app.product.serializers import ProductVariantSerializer
from app.authorization.serializers import UserSimpleSerializer, UserSerializer
from app.coupon.models import Coupon
from app.payment.models import Payment
from app.payment.serializers import PaymentSerializer

class CheckoutSerializer(serializers.ModelSerializer):

    day = serializers.DateField()

    time = serializers.TimeField()

    adult_quantity = serializers.IntegerField(default=0, min_value=0, max_value=9999)

    child_quantity = serializers.IntegerField(default=0, min_value=0, max_value=9999)

    variantID = serializers.CharField(max_length=16)

    relatedID = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=64)

    couponID = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=128)

    adult_price = serializers.SerializerMethodField()

    child_price = serializers.SerializerMethodField()

    offer = serializers.SerializerMethodField()

    total = serializers.SerializerMethodField()

    product = serializers.SerializerMethodField(method_name='get_product_name')

    variant = serializers.SerializerMethodField(method_name='get_variant_name')

    class Meta:
        model = Order 
        fields = (
            'day', 'time', 'adult_quantity', 'child_quantity', 'variantID', 'relatedID', 'couponID', 'adult_price', 'child_price', 'offer', 'total', 'product', 'variant'
        )

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
        variant = self.get_variant(obj)
        return variant.adult_price[self.get_price_lelve()] * obj['adult_quantity']

    def get_adult_unit_price(self, obj):
        variant = self.get_variant(obj)
        return variant.adult_price[self.get_price_lelve()]

    def get_child_price(self, obj):
        variant = self.get_variant(obj)
        return variant.child_price[self.get_price_lelve()] * obj['child_quantity']

    def get_child_unit_price(self, obj):
        variant = self.get_variant(obj)
        if variant.child_status:
            return variant.child_price[self.get_price_lelve()]
        return Decimal(0.0)

    def get_offer(self, obj):
        coupon = self.get_coupon(obj)
        if coupon:
            return coupon.amount * obj['adult_quantity']

        return Decimal(0.0)

    def get_total(self, obj):
        total = Decimal(self.get_adult_price(obj)) + Decimal(self.get_child_price(obj)) - Decimal(self.get_offer(obj))
        if total < 0 :
            return Decimal(0.0)
        return total

    def get_product_name(self, obj):
        return self.get_product(obj).title

    def get_variant_name(self, obj):
        return self.get_variant(obj).name

    def get_variant(self, validate_data):
        try:
            return ProductVariant.objects.get(variantID=validate_data['variantID'])
        except ProductVariant.DoesNotExist:
            return None

    def get_product(self, validate_data):
        return self.get_variant(validate_data).product

    def get_coupon(self, validate_data):
        couponID = validate_data.get('couponID', None)

        if couponID:
            try:
                return Coupon.objects.get(couponID=validate_data['couponID'])
            except Coupon.DoesNotExist:
                return None
        
        return None

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

    def validate_variantID(self, value):
        try:
            variant = ProductVariant.objects.get(variantID=value)
            if not variant.status or not variant.product.status:
                raise serializers.ValidationError('此产品已下架')
        except ProductVariant.DoesNotExist:
            raise serializers.ValidationError('产品不存在')

        return value

    def validate_relatedID(self, value):
        if value:
            if not Order.objects.filter(orderID=value).exists():
                raise serializers.ValidationError('UGO关联单号不存在')
        return value

    def validate_couponID(self, value):
        if value:
            try:
                coupon = Coupon.objects.get(couponID=value)
                if not coupon.enable:
                    raise serializers.ValidationError('优惠券已失效')
                
                if not coupon.validate_exp():
                    raise serializers.ValidationError('优惠券已过期')

                if not coupon.customer.filter(id=self.get_user().id).exists():
                    raise serializers.ValidationError('优惠券非法')

            except Coupon.DoesNotExist:
                raise serializers.ValidationError('优惠券不存在')
                
        return value

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

    order_status = serializers.ReadOnlyField()

    create_at = serializers.ReadOnlyField()

    change_at = serializers.ReadOnlyField()

    adult_price = serializers.ReadOnlyField()

    adult_unit_price = serializers.ReadOnlyField()

    child_price = serializers.ReadOnlyField()

    child_unit_price = serializers.ReadOnlyField()

    offer = serializers.ReadOnlyField()

    total = serializers.ReadOnlyField()

    remark = serializers.ReadOnlyField()

    product = serializers.ReadOnlyField()

    productID = serializers.ReadOnlyField()

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

    guest_relatedID = serializers.CharField(required=False, allow_null=True, allow_blank=True, max_length=64)

    class Meta:
        model = Order 
        fields = '__all__'

    @transaction.atomic
    def create(self, validate_data):
        adult_price = self.get_adult_price(validate_data)
        adult_unit_price = self.get_adult_unit_price(validate_data)
        child_price = self.get_child_price(validate_data)
        child_unit_price = self.get_child_unit_price(validate_data)
        offer = self.get_offer(validate_data)
        total = self.get_total(validate_data)
        product = self.get_product(validate_data)
        productID = product.productID
        variant = self.get_variant(validate_data)
        customer = self.get_user()

        couponID = validate_data.pop('couponID')

        order = Order.objects.create(**validate_data,
            adult_price=adult_price,
            adult_unit_price=adult_unit_price,
            child_price=child_price,
            child_unit_price=child_unit_price,
            offer=offer,
            total=total,
            product=product.title,
            productID=productID,
            variant=variant.name,
            category=product.category,
            sku=variant.sku,
            customer=customer.username,
            customer_id=customer.id
        )

        payment = Payment.objects.create(
            total=total,
            captured=total,
            order_id=order.id,
            customer=customer.username,
            customer_id=customer.id,
            customer_balance=customer.balance
        )

        payment.capture(self.get_user(), total)

        return order

class OrderUpdateSerializer(OrderCreateSerializer):

    day = serializers.ReadOnlyField()

    time = serializers.ReadOnlyField()

    adult_quantity = serializers.ReadOnlyField()

    child_quantity = serializers.ReadOnlyField()

    variantID = serializers.ReadOnlyField()

    order_from = serializers.ReadOnlyField()

    relatedID = serializers.ReadOnlyField()

    guest_relatedID = serializers.ReadOnlyField()

    is_delete = serializers.BooleanField(required=False, default=False)

    remark = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    order_status = serializers.IntegerField(required=False)

    payment = serializers.SerializerMethodField()

    class Meta:
        model = Order 
        fields = '__all__'

    def validate(self, validate_data):
        return validate_data

    def get_payment(self, obj):
        query = Payment.objects.filter(order_id=obj.id)
        serializer = PaymentSerializer(instance=query, many=True, context=self.context)
        return serializer.data
        
    @transaction.atomic
    def update(self, instance, validated_data):
        if instance.operator is None or instance.operator_id is None:
            if self.get_user().is_staff:
                instance.operator = self.get_user().username
                instance.operator_id = self.get_user().id
                instance.save()

        return super().update(instance, validated_data)
