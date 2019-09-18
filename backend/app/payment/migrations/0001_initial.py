# Generated by Django 2.2.4 on 2019-09-18 09:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0006_remove_order_pay_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default='0.0', max_digits=9)),
                ('currency', models.CharField(default='USD', max_length=10)),
                ('status', models.CharField(choices=[(0, '未支付'), (1, '部分支付'), (2, '全部付清'), (3, '部分退款'), (4, '全部退款')], default=2, max_length=10)),
                ('extra_data', models.TextField(blank=True, default='')),
                ('token', models.CharField(blank=True, default=uuid.UUID('6686d3cf-1440-493b-a492-fc57f76a4187'), max_length=36)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('change_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, default='')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment', to='order.Order')),
            ],
            options={
                'db_table': 'payment',
                'ordering': ['-id'],
            },
        ),
    ]
