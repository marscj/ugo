from rest_framework import  serializers

from .models import Price
from app.authorization.serializers import UserSerializer
from app.product.serializers import ProductVariant

class PriceSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    variant = ProductVariant(read_only=True)

    user_id = serializers.IntegerField(required=True, write_only=True)

    variant_id = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        model = Price
        fields = '__all__'

     def create(self, validated_data):
        user = validated_data.pop('user_id', None)
        variant = validated_data.pop('variant_id', None)
        
        return Price.objects.create(**validated_data, user_id=user, variant_id=variant)