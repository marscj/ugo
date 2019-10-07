default_app_config = 'app.booking.apps.BookingConfig'

class BookingStatus:
    INQUIRY = 1
    CONFIRM = 2
    PENDING = 3
    SENT = 4
    OP_CANCELLED = 5
    OP_APPROVED = 6

    CHOICE = (
        (INQUIRY, '查询'),
        (CONFIRM, '确认'),
        (PENDING, '等待'),
        (SENT, '发送'),
        (OP_CANCELLED, '操作取消'),
        (OP_APPROVED, '操作通过')
    )

class BookingCategory:
    Restaurant = 1
    Tour = 2
    Transport = 3
    Car = 4
    Hotel = 5
    Gift = 6

    CHOICE = (
        (Restaurant, '餐厅'),
        (Tour, '旅游'),
        (Transport, '交通'),
        (Car, '租车'),
        (Hotel, '酒店'),
        (Gift, '礼物'),
    )