from django.db import models

# Create your models here.
class Cart(models.Model):
    
    day = models.DateField(blank=True, null=True)

    start_time = models.TimeField(blank=True, null=True)

    end_time = models.TimeField(blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True)

    change_at = models.DateTimeField(auto_now=True)

    remark = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'cart'