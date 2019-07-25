from rest_framework import  serializers

from .models import Price
from app.authorization.serializers import UserSimpleSerializer

class PriceSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    variant = serializers.PrimaryKeyRelatedField(read_only=True)

    user_id = serializers.IntegerField()

    variant_id = serializers.IntegerField()

    curLev = serializers.IntegerField(min_value=1, max_value=5)

    lv1 = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.0)

    lv2 = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.0)

    lv3 = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.0)

    lv4 = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.0)

    lv5 = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.0)

    class Meta:
        model = Price
        fields = '__all__'