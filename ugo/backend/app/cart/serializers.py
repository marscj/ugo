# from rest_framework import  serializers

# from .models import Cart
# from app.product.serializers import ProductVariantSerializer

# class CartSerializer(serializers.ModelSerializer):

#     day = serializers.DateField(required=True)

#     startTime = serializers.TimeField(required=True)

#     endTime = serializers.TimeField(required=True)

#     adultQuantity = serializers.PositiveIntegerField(required=False, null=True, validators=[MinValueValidator(0)])

#     childQuantity = serializers.PositiveIntegerField(required=False, null=True, validators=[MinValueValidator(0)])

#     product = models.ForeignKey(ProductVariant, blank=True, null=True, related_name='cart', on_delete=models.CASCADE)

#     user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='cart', on_delete=models.SET_NULL)

#     remark = models.TextField(blank=True, null=True)

#     class Meta:
#         model = Cart
#         fields = '__all__'