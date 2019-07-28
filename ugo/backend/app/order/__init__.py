
class OrderStatus:
    CREATE = 0
    CONFIRM = 1
    SUCCESS = 2
    FAILURE = 3
    CANCEL = 4

    CHOICE = (
        (CREATE, '新建'),
        (CONFIRM, '订单已确认'),
        (SUCCESS, '出票成功'),
        (FAILURE, '出票失败'),
        (CANCEL, '订单已取消')
    )