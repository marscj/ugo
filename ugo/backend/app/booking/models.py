from django.db import models

class Booking(models.Model):

    # 预定号
    bookingId = models.CharField(blank=True, null=True, max_length=32, unique=True)

    # 确认号
    confirmId = models.CharField(blank=True, null=True, max_length=64, unique=True)

    # 创建时间
    createAt = models.DateTimeField(auto_now_add=True)

    # 修改时间
    changeAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'booking'