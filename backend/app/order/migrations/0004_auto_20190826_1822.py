# Generated by Django 2.2.4 on 2019-08-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20190826_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='productID',
        ),
        migrations.RemoveField(
            model_name='order',
            name='variantID',
        ),
        migrations.AddField(
            model_name='order',
            name='product_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='variant_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]