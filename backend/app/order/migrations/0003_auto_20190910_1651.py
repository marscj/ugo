# Generated by Django 2.2.4 on 2019-09-10 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_order_confirmid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(0, '新建'), (1, '订单已确认'), (2, '出票成功'), (3, '订单已取消'), (4, '退款中'), (5, '已退款')], default=0),
        ),
    ]