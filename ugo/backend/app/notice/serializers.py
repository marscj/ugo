from rest_framework import  serializers

from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=128)
    subtitle = serializers.CharField(max_length=256)
    content = serializers.CharField(max_length=2048)

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
