# Generated by Django 2.2 on 2019-07-03 12:17

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
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingId', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('confirmId', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('day', models.DateField(blank=True, null=True)),
                ('startTime', models.TimeField(blank=True, null=True)),
                ('endTime', models.TimeField(blank=True, null=True)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('changeAt', models.DateTimeField(auto_now=True)),
                ('adultQuantity', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('childQuantity', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('remark', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='product.ProductVariant')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
