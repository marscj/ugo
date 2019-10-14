# Generated by Django 2.2 on 2019-10-14 05:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingID', models.CharField(blank=True, max_length=64, null=True)),
                ('groupID', models.CharField(blank=True, max_length=64, null=True)),
                ('booking_date', models.DateField(blank=True, null=True)),
                ('action_date', models.DateField(blank=True, null=True)),
                ('action_time', models.TimeField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('product', models.CharField(blank=True, max_length=256, null=True)),
                ('itinerary', models.TextField(blank=True, null=True)),
                ('category', models.IntegerField(choices=[(1, '餐厅'), (2, '旅游'), (3, '交通'), (4, '酒店')], default=2)),
                ('quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('child_quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('free_quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('child_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('cost_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('child_cost_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('total_cost_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('vat', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('blocked_room', models.CharField(blank=True, max_length=128, null=True)),
                ('sgl', models.IntegerField(blank=True, default=0, null=True)),
                ('sgl_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('sgl_cost_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('dbl', models.IntegerField(blank=True, default=0, null=True)),
                ('dbl_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('dbl_cost_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('twn', models.IntegerField(blank=True, default=0, null=True)),
                ('twn_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('twn_cost_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('tpl', models.IntegerField(blank=True, default=0, null=True)),
                ('tpl_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('tpl_cost_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('exb', models.IntegerField(blank=True, default=0, null=True)),
                ('exb_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('exb_cost_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('tourism_fees', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('rate_room', models.CharField(blank=True, max_length=128, null=True)),
                ('conf_list', models.FileField(blank=True, null=True, upload_to='conf')),
                ('room_list', models.FileField(blank=True, null=True, upload_to='room')),
                ('room_update', models.DateField(blank=True, null=True)),
                ('emailed', models.DateField(blank=True, null=True)),
                ('cancel_policy', models.TextField(blank=True, null=True)),
                ('cancel_date', models.DateField(blank=True, null=True)),
                ('nights', models.IntegerField(blank=True, default=0, null=True)),
                ('rooms', models.IntegerField(blank=True, default=0, null=True)),
                ('payment_due_date', models.DateField(blank=True, null=True)),
                ('ref', models.TextField(blank=True, null=True)),
                ('pick_up_time', models.DateTimeField(blank=True, null=True)),
                ('pick_up_address', models.CharField(blank=True, max_length=256, null=True)),
                ('drop_off_address', models.CharField(blank=True, max_length=256, null=True)),
                ('driver', models.CharField(blank=True, max_length=150, null=True)),
                ('driver_mobile', models.CharField(blank=True, max_length=150, null=True)),
                ('vehicle', models.CharField(blank=True, max_length=64, null=True)),
                ('vehicle_model', models.CharField(blank=True, max_length=64, null=True)),
                ('guide', models.CharField(blank=True, max_length=150, null=True)),
                ('guide_mobile', models.CharField(blank=True, max_length=16, null=True)),
                ('operator', models.CharField(blank=True, max_length=150, null=True)),
                ('officer', models.CharField(blank=True, max_length=150, null=True)),
                ('status', models.IntegerField(choices=[(1, '查询'), (2, '确认'), (3, '等待'), (4, '发送'), (5, '操作取消'), (6, '操作通过')], default=1)),
                ('remark', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('change_at', models.DateTimeField(auto_now=True, null=True)),
                ('supplier', models.CharField(blank=True, max_length=64, null=True)),
                ('order_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'booking',
                'ordering': ['-id'],
            },
        ),
    ]
