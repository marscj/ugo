from rest_framework import  serializers

from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=128, min_length=5, allow_null=False)
    subtitle = serializers.CharField(max_length=256, min_length=5, allow_null=False)
    content = serializers.CharField(max_length=2048, min_length=5, allow_null=False)
 
    class Meta:
        model = Notice 
        fields = '__all__'

class NoticeReadOnlySerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField()
    subtitle = serializers.ReadOnlyField()
    content = serializers.ReadOnlyField()

    class Meta:
        model = Notice 
        fields = '__all__'
