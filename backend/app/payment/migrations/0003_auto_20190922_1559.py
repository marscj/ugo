# Generated by Django 2.2 on 2019-09-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_payment_captured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='captured',
            field=models.DecimalField(decimal_places=2, default='0.0', max_digits=10),
        ),
        migrations.AlterField(
            model_name='payment',
            name='total',
            field=models.DecimalField(decimal_places=2, default='0.0', max_digits=10),
        ),
    ]
