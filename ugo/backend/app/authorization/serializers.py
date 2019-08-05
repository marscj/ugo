from rest_framework import  serializers
from django.contrib.auth import password_validation
from rest_framework.validators import UniqueValidator

from .models import CustomUser, Role, Permission, ActionEntity

class ActionEntitySerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    
    class Meta:
        model = ActionEntity
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):

    actionEntitySet = ActionEntitySerializer(many=True)

    class Meta:
        model = Permission
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()

    permissions = PermissionSerializer(many=True)

    name = serializers.CharField(max_length=32, validators=[UniqueValidator(queryset=Role.objects.all())])

    status = serializers.IntegerField() 

    describe = serializers.CharField(required=False, allow_null=True, max_length=128)

    class Meta:
        model = Role
        fields = '__all__'

    def create(self, validated_data):
        permissions = validated_data.pop('permissions', None)
        role = Role.objects.create(**validated_data)
        # if permissions is not None:
        #     for permissionData in permissions:
        #         permission = Permission.objects.create(**permissionData, role=role)
        #         for actionData in permissionData.get('actionEntitySet'):
        #             ActionEntity.objects.create(**actionData, permission=permission)
        return role

    def update(self, instance, validated_data):
        permissions = validated_data.pop('permissions', None)
        for permissionData in permissions:
            for actionData in permissionData.get('actionEntitySet'):
                action = ActionEntity.objects.get(pk=actionData.get('id'))
                action.enable = actionData.get('enable')
                action.save()

        super().update(instance, validated_data)

        return instance

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