
class OrderStatus:
    CREATE = 0
    CONFIRM = 1
    PADDING = 2
    CANCEL = 3

    CHOICE = (
        (CREATE, '新建'),
        (CONFIRM, '订单已确认'),
        (PADDING, '等待'),
        (CANCEL, '订单已取消')
    )