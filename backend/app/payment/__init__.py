default_app_config = 'app.payment.apps.PaymentConfig'

class PaymentStatus:
    UNPAID = 0
    PARTIALLY_PAID = 1
    FULLY_PAID = 2
    REFUNDEDING = 3
    PARTIALLY_REFUNDED = 4
    FULLY_REFUNDED = 5

    CHOICES = (
        (UNPAID, '未支付'),
        (PARTIALLY_PAID, '部分支付'),
        (FULLY_PAID, '全部付清'),
        (REFUNDEDING, '退款中'),
        (PARTIALLY_REFUNDED, '部分退款'),
        (FULLY_REFUNDED, '全部退款')
    )


class PaymentAction:
    CAPTURE = 0
    REFUNDED = 1
    RECHARGE = 2

    CHOICES = (
        (CAPTURE, '捕捉'),
        (REFUNDED, '退款'),
        (RECHARGE, '充值'),
    )