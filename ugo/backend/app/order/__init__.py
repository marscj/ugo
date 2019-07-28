
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

class PayStatus:
    UNPAID = 0
    PARTIALLY_PAID = 1
    FULLY_PAID = 2
    PARTIALLY_REFUNDED = 3
    FULLY_REFUNDED = 4

    CHOICE = (
        (UNPAID, '未支付'),
        (PARTIALLY_PAID, '部分支付'),
        (FULLY_PAID, '全部付清'),
        (PARTIALLY_REFUNDED, '部分退款'),
        (FULLY_REFUNDED, '全部退款')
    )