# Generated by Django 2.2 on 2019-08-04 10:00

import app.order.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderID', models.CharField(default=app.order.models.create_uuid, max_length=64)),
                ('confirmID', models.CharField(blank=True, max_length=64, null=True)),
                ('order_status', models.IntegerField(choices=[(0, '新建'), (1, '订单已确认'), (2, '出票成功'), (3, '出票失败'), (4, '订单已取消')], default=0)),
                ('pay_status', models.IntegerField(choices=[(0, '未支付'), (1, '部分支付'), (2, '全部付清'), (3, '部分退款'), (4, '全部退款')], default=0)),
                ('day', models.DateField()),
                ('time', models.TimeField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('change_at', models.DateTimeField(auto_now=True)),
                ('customer_info', models.TextField(blank=True, null=True)),
                ('customer_contact', models.TextField(blank=True, null=True)),
                ('adult_quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('adult_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('child_quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('child_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('remark', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_custom', to=settings.AUTH_USER_MODEL)),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_operator', to=settings.AUTH_USER_MODEL)),
                ('variant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='product.ProductVariant')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
