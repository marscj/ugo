default_app_config = 'app.booking.apps.BookingConfig'

class BookingStatus:
    INQUIRY = 1
    CONFIRM = 2
    PENDING = 3
    SENT = 4
    OP-CANCELLED = 5
    OP-APPROVED = 6

    CHOICE = (
        (INQUIRY, '查询'),
        (CONFIRM, '确认'),
        (PENDING, '等待'),
        (SENT, '发送'),
        (OP-CANCELLED, '操作取消'),
        (OP-APPROVED, '操作通过')
    )