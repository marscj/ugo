from rest_framework.permissions import BasePermission
from rest_framework import exceptions
from app.authorization.models import CustomUser

def has_permission(request, permissionId):
    perms_map = [
        'query',
        'add',
        'edit',
        'delete',
        'staff',
    ]

    return request.user.role.permissions.filter(permissionId=permissionId).filter(actionEntitySet__action__in=perms_map).exists()

class MiddlewarePermission(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and isinstance(request.user, CustomUser): 
            if request.user.role is not None and request.user.role.status == 0:
                return has_permission(request, view.permissionId)
                
        return False

class MiddlewareLoginPermission(BasePermission):

    def has_permission(self, request, view):
        username = request.data.get('username', None)
 
        if username is not None:
            try:
                request.user = CustomUser.objects.get(username=username)
                return has_permission(request, view.permissionId)
            except CustomUser.DoesNotExist:
                raise exceptions.ValidationError({'username': '没有找到该用户'})
                
        return True