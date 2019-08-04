from rest_framework import  serializers
from django.contrib.auth import password_validation

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

    # def create(self, validated_data):
    #     permissions = validated_data.pop('permissions', None)
    #     product = Role.objects.create(**validated_data)
        
    #     if permissions is not None:
    #         for permission in permissions:
    #             for action in permission.actionEntitySet:
    #                 ActionEntity.objects.create(**action)
    #             _permission = data.objects.create(**permission)
    #             product.permissions.add(_permission)

    #     return product

    # def update(self, instance, validated_data):
    #     permissions = validated_data.pop('permissions', None)

    #     for data in instance.permissions.all():
    #         instance.permissions.remove(data)
    #         data.delete()

    #     if permissions is not None:
    #         for data in permissions:
    #             _data = data.objects.create(**data)
    #             instance.permissions.add(_data)

    #     super().update(instance, validated_data)

    #     return instance

class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def get_current_user(self):
        return self.context['request'].user

    def validate(self, data):
        old_password = data.get('old_password', None)
        new_password = data.get('new_password', None)

        if old_password is not None and not self.get_current_user().check_password(old_password):
            raise serializers.ValidationError({'old_password': 'Your old password was entered incorrectly. Please enter it again.'})
                
        if new_password is not None:
            password_validation.validate_password(new_password)

        return super().validate(data)

class UserCreateSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)
    
    role_id = serializers.IntegerField(required=False)

    class Meta:
        model = CustomUser
        fields = '__all__'

    def validate(self, data):
        password = data.get('password', None)
                
        if password is not None:
            password_validation.validate_password(password)

        return super().validate(data)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):

    role = RoleSerializer(read_only=True)

    role_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = CustomUser
        exclude = (
            'password',
        )

    def update(self, instance, validated_data):
        validated_data.pop('password', None)
        return super().update(instance, validated_data)

class UserSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id', 'username', 'price_level'
        )