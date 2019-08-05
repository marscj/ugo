from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete

from .models import Role, Permission, ActionEntity

def create_permission(permissionId, permissionName, actions, role):
    permission = Permission.objects.create(permissionId=permissionId, permissionName=permissionName, role=role)

    for action in actions:
        ActionEntity.objects.create(action=action['action'], label=action['label'], enable=False, permission=permission)

@receiver(post_save, sender=Role)
def role_model_post_save(sender, instance, created, **kwargs):
    if created:
        create_permission('Staff', 'Staff', [
            {
                'action': 'query',
                'label': '登陆到后台'
            }
        ], instance)

        create_permission('CustomUser', 'User', [
            {
                'action': 'query',
                'label': '查询'
            },
            {
                'action': 'add',
                'label': '新增'
            },
            {
                'action': 'edit',
                'label': '编辑'
            },
            {
                'action': 'delete',
                'label': '删除'
            }
        ], instance)

        create_permission('Role', 'Role', [
            {
                'action': 'query',
                'label': '查询'
            },
            {
                'action': 'add',
                'label': '新增'
            },
            {
                'action': 'edit',
                'label': '编辑'
            },
            {
                'action': 'delete',
                'label': '删除'
            }
        ], instance)

        create_permission('Product', 'Product', [
            {
                'action': 'query',
                'label': '查询'
            },
            {
                'action': 'add',
                'label': '新增'
            },
            {
                'action': 'edit',
                'label': '编辑'
            },
            {
                'action': 'delete',
                'label': '删除'
            }
        ], instance)

        create_permission('Order', 'Order', [
            {
                'action': 'query',
                'label': '查询'
            },
            {
                'action': 'add',
                'label': '新增'
            },
            {
                'action': 'edit',
                'label': '编辑'
            },
            {
                'action': 'delete',
                'label': '删除'
            }
        ], instance)
        