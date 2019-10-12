default_app_config = 'app.booking.apps.BookingConfig'

class BookingStatus:
    Inquiry = 1
    Confirm = 2
    Padding = 3
    Email_Sent = 4
    OP_Cancelled = 5
    OP_Approved =6

    CHOICE = (
        (Inquiry, '查询'),
        (Confirm, '确认'),
        (Padding, '等待'),
        (Email_Sent, '发送'),
        (OP_Cancelled, '操作取消'),
        (OP_Approved, '操作通过')
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

class RoomStatus:
    Inquiry = 1
    Confirm = 2
    Room_Blocked = 3
    Email_Sent = 4
    OP_Cancelled = 5
    Roomlist_Sent = 6
    Inquriy_Sent = 7
    AC_Paid = 8
    AC_Pending = 9

    CHOICE = (
        (Inquiry, '查询'),
        (Confirm, '确认'),
        (Room_Blocked, '房间锁定'),
        (Email_Sent, '邮件已发送'),
        (OP_Cancelled, '操作取消'),
        (Roomlist_Sent, '房间列表发送'),
        (Inquriy_Sent, '查询发送'),
        (AC_Paid, 'AC Paid'),
        (AC_Pending, 'AC Pending'),
    )