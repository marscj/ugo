# Generated by Django 2.2.4 on 2019-09-18 11:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20190918_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='token',
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True),
        ),
    ]
