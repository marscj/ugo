# Generated by Django 2.2.4 on 2019-09-18 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
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
