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

class MealPeriod:
    BREAKFAST = 1
    LUNCH = 2
    DINNER = 3
    AFTERNOON_TEA = 4

    CHOICE = (
        (BREAKFAST, '早餐'),
        (LUNCH, '午餐'),
        (DINNER, '晚餐'),
        (AFTERNOON_TEA, '下午茶'),
    )