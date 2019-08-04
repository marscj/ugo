# Generated by Django 2.2 on 2019-08-04 10:00

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('source', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('category', models.IntegerField(choices=[(1, '美食'), (2, '门票'), (3, '日游'), (4, '用车'), (5, '酒店'), (6, '伴手礼')], default=1)),
                ('productID', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('title', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=128, null=True)),
                ('special', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=32, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('gallery', models.ManyToManyField(blank=True, related_name='gallery', to='source.ProductImage')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photo', to='source.ProductImage')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('variantID', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('sku', models.CharField(max_length=32, unique=True)),
                ('adult_status', models.BooleanField(default=True)),
                ('adult_desc', models.CharField(blank=True, max_length=64, null=True)),
                ('adult_quantity', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('adult_price', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=2, max_digits=10), size=5)),
                ('child_status', models.BooleanField(default=False)),
                ('child_desc', models.CharField(blank=True, max_length=64, null=True)),
                ('child_quantity', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('child_price', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=2, max_digits=10), size=5)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variant', to='product.Product')),
            ],
            options={
                'db_table': 'variant',
            },
        ),
    ]
