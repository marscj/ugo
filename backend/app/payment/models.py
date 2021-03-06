from django.db import models, transaction

from .import PaymentStatus, PaymentAction
from app.authorization.models import CustomUser
class Payment(models.Model):
   
    #金额
    total = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')

    #捕捉金额
    captured = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')

    #货币
    currency = models.CharField(max_length=10, default='USD')

    #状态
    status = models.IntegerField(choices=PaymentStatus.CHOICES, default=PaymentStatus.UNPAID)

    #订单类型
    action = models.IntegerField(choices=PaymentAction.CHOICES, default=PaymentAction.CAPTURE)

    #附加数据
    extra_data = models.TextField(blank=True, default='')

    #创建时间
    create_at = models.DateTimeField(auto_now_add=True)

    #修改时间
    change_at = models.DateTimeField(auto_now=True)

    #说明
    description = models.TextField(blank=True, null=True)

    #订单id
    order_id = models.IntegerField(blank=True, null=True)
    
    #客户username
    customer = models.CharField(blank=True, null=True, max_length=150)

    #客户ID
    customer_id = models.IntegerField(blank=True, null=True)
    
    #客户额度
    customer_balance = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')

    class Meta:
        db_table = 'payment'
        ordering = ['-id']

    @transaction.atomic
    def refund(self):
        customer = CustomUser.objects.get(pk=self.customer_id)
        customer.recharge(self.total)

        self.captured = self.total
        self.status = PaymentStatus.FULLY_REFUNDED
        self.customer_balance = customer.balance

        self.save()
        

           
        