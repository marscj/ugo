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

    role = RoleSerializer(many=False)

    class Meta:
        model = CustomUser
        # fields = '__all__'
        exclude = (
            'password',
        )

class UserSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id', 'username'
        )