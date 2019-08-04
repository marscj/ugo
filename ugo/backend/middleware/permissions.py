from rest_framework.permissions import BasePermission
from rest_framework import exceptions
from app.authorization.models import CustomUser

def has_permission(request, permissionId):
    perms_map = {
        'GET': 'query',
        'POST': 'add',
        'PUT': 'edit',
        'DELETE': 'delete'
    }
    
    if request.method not in perms_map:
        raise exceptions.MethodNotAllowed(request.method)

    return request.user.role.permissions.filter(permissionId=permissionId).filter(actionEntitySet__action=perms_map[request.method]).exists()

class IsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and isinstance(request.user, CustomUser): 
            if request.user.role is not None and request.user.role.status == 0:
                return has_permission(request, view.get_queryset().model.__name__)
                
        return False