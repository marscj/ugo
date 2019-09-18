# Generated by Django 2.2.4 on 2019-09-18 11:29

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('describe', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'role',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissionId', models.CharField(blank=True, max_length=32, null=True)),
                ('permissionName', models.CharField(blank=True, max_length=32, null=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='authorization.Role')),
            ],
            options={
                'db_table': 'permission',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ActionEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(blank=True, max_length=32, null=True)),
                ('label', models.CharField(blank=True, max_length=32, null=True)),
                ('enable', models.BooleanField(default=False)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actionEntitySet', to='authorization.Permission')),
            ],
            options={
                'db_table': 'action',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, default='', max_length=16, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('price_level', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='authorization.Role')),
            ],
            options={
                'db_table': 'user',
                'ordering': ['-id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
