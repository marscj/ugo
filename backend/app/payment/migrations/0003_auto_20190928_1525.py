# Generated by Django 2.2 on 2019-09-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20190928_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='action',
            field=models.IntegerField(choices=[(0, '扣费'), (1, '退款'), (2, '充值')], default=0),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.IntegerField(choices=[(0, '未支付'), (1, '部分支付'), (2, '全部付清'), (3, '退款中'), (4, '部分退款'), (5, '全部退款')], default=0),
        ),
    ]
