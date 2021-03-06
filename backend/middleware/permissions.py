from django.db.models import Q
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import exceptions
from app.authorization.models import CustomUser

def has_permission(request, permissionId):
    perms_map = {
        'GET': 'query',
        'POST': 'add',
        'PUT': 'edit',
        'DELETE': 'delete',
    }

    if request.method not in ['GET', 'POST', 'PUT', 'DELETE']:
        raise exceptions.MethodNotAllowed(method)
    
    query = request.user.role.permissions.filter(
        Q(permissionId=permissionId) & 
        Q(actionEntitySet__action=perms_map[request.method]) &
        Q(actionEntitySet__enable=True)
    )

    return query

def custom_permission(request, view):
    if request.user and request.user.is_authenticated and isinstance(request.user, CustomUser): 
            if request.user.role is not None and request.user.role.status == 0:
                return has_permission(request, view.permissionId)
    
    return False

class BackendPermission(BasePermission):
    def has_permission(self, request, view):
        return custom_permission(request, view)

class BackendLoginPermission(BasePermission):

    def has_permission(self, request, view):
        username = request.data.get('username', None)
 
        if username is not None:
            try:
                user = CustomUser.objects.get(username=username)
                
                return user.role.permissions.filter(
                    Q(permissionId='Staff') &
                    Q(actionEntitySet__action='query') & 
                    Q(actionEntitySet__enable=True)
                ).exists()

            except CustomUser.DoesNotExist:
                raise exceptions.ValidationError({'detail': '没有找到该用户'})
                
        return True

class BackendOrSafePermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return custom_permission(request, view)

        return False