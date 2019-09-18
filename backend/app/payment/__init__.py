default_app_config = 'app.payment.apps.PaymentConfig'

class PaymentStatus:
    UNPAID = 0
    PARTIALLY_PAID = 1
    FULLY_PAID = 2
    PARTIALLY_REFUNDED = 3
    FULLY_REFUNDED = 4

    CHOICES = (
        (UNPAID, '未支付'),
        (PARTIALLY_PAID, '部分支付'),
        (FULLY_PAID, '全部付清'),
        (PARTIALLY_REFUNDED, '部分退款'),
        (FULLY_REFUNDED, '全部退款')
    )