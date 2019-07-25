# Generated by Django 2.2 on 2019-07-25 12:48

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20190725_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='adult_price',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=2, max_digits=10), size=5),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='child_price',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=2, max_digits=10), size=5),
        ),
    ]
