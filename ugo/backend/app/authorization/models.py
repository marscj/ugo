from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, UserManager, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

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

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        db_table = 'user'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

class UserProfile(models.Model):
    
    userId = models.IntegerField()

    class Meta:
        db_table = 'user_profile'