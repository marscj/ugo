# Generated by Django 2.2 on 2019-07-01 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0006_auto_20190701_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, related_name='role', to='authorization.Permission'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='actionEntitySet',
            field=models.ManyToManyField(blank=True, related_name='permission', to='authorization.ActionEntity'),
        ),
    ]
