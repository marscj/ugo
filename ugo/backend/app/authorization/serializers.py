from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import  serializers

from .models import CustomUser, Role, Permission, ActionEntity

class ActionEntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ActionEntity
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):

    actionEntitySet = ActionEntitySerializer(many=True)

    class Meta:
        model = Permission
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):

    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(required=False, write_only=True)

    role = RoleSerializer(read_only=True)

    role_id = serializers.IntegerField(required=False)

    class Meta:
        model = CustomUser
        fields = '__all__'

    def validate(self, data):
        password = data.get('password', None)
        if password is not None:
            validate_password(password)
        
        return super().validate(data)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
    
        if password is not None and instance.check_password(password):
            instance.set_password(password)

        return super().update(instance, validated_data)

class UserSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id', 'username', 'price_level'
        )