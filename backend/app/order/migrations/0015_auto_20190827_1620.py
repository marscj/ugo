# Generated by Django 2.2.4 on 2019-08-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20190827_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='productID',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='variantID',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]