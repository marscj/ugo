from .models import Permission, ActionEntity

def per_create_permission(permissionId, permissionName, actions, role):
        permission = Permission.objects.create(permissionId=permissionId, permissionName=permissionName, role=role)

        for action in actions:
            ActionEntity.objects.create(action=action['action'], label=action['label'], enable=False, permission=permission)

def create_permission(instance):
    per_create_permission('Staff', 'Staff', [
        {
            'action': 'query',
            'label': '登陆到后台'
        }
    ], instance)

    per_create_permission('CustomUser', 'User', [
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

    per_create_permission('Role', 'Role', [
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

    per_create_permission('Product', 'Product', [
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

    per_create_permission('Order', 'Order', [
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

    per_create_permission('Coupon', 'Coupon', [
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

    per_create_permission('Booking', 'Booking', [
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

    per_create_permission('Payment', 'Payment', [
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

def create_permission_9_24(instance):
    per_create_permission('Coupon', 'Coupon', [
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

    per_create_permission('Booking', 'Booking', [
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

    per_create_permission('Payment', 'Payment', [
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