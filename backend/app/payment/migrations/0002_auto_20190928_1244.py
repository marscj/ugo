# Generated by Django 2.2 on 2019-09-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='action',
            field=models.CharField(choices=[(0, '扣费'), (1, '退款'), (2, '充值')], default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='payment',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]