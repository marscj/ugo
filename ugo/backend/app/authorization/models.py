from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, UserManager, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinValueValidator, MaxValueValidator

from jsonfield import JSONField,JSONCharField

from .import UserType

class CustomUser(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={'unique': 'A user with that username already exists.'}
    )
    email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone = models.CharField(blank=True, null=True, default='', max_length=16)
    date_joined = models.DateTimeField(default=timezone.now)

    name = models.CharField(blank=True, null=True, max_length=32)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatars')
    user_type = models.IntegerField(default=UserType.Customer, choices=UserType.CHOISE)
    price_level = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    balance = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    
    role = models.ForeignKey('Role', blank=True, null=True, related_name='user', on_delete=models.SET_NULL)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

class Role(models.Model):
    name = models.CharField(blank=True, null=True, max_length=32)
    describe = models.CharField(blank=True, null=True, max_length=128)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = 'role'

class Permission(models.Model):
    permissionId = models.CharField(blank=True, null=True, max_length=32)
    permissionName = models.CharField(blank=True, null=True, max_length=32)
    role = models.ForeignKey(Role, related_name='permissions', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'permission'

class ActionEntity(models.Model):
    action = models.CharField(blank=True, null=True, max_length=32)
    describe = models.CharField(blank=True, null=True, max_length=32)
    permission = models.ForeignKey(Permission, related_name='actionEntitySet', on_delete=models.CASCADE)

    class Meta:
        db_table = 'action'