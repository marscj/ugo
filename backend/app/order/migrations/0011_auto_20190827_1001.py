# Generated by Django 2.2.4 on 2019-08-27 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20190826_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.AddField(
            model_name='order',
            name='order_from',
            field=models.CharField(blank=True, default='ugodubai', max_length=64, null=True),
        ),
    ]
