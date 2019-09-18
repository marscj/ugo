default_app_config = 'app.order.apps.OrderConfig'

class OrderStatus:
    CREATE = 0
    CONFIRM = 1
    SUCCESS = 2
    CANCEL = 3
    REFUNDING = 4
    REFUNDED = 5

    CHOICE = (
        (CREATE, '新建'),
        (CONFIRM, '订单已确认'),
        (SUCCESS, '出票成功'),
        (CANCEL, '订单已取消'),
        (REFUNDING, '退款中'),
        (REFUNDED, '已退款')
    )