from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from accounts.managers import CustomUserManager, PhoneNumberValidationManager


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class GenderTypes(models.IntegerChoices):
        MALE = 1
        FEMALE = 2

    gender = models.SmallIntegerField(choices=GenderTypes.choices, default=GenderTypes.MALE)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class PhoneNumberValidation(models.Model):
    """
    This model save phone number and validation code to verify user phone number,
    and creation_date field for checking time of verifying user.
    """
    phone_number = models.CharField(max_length=10)
    validation_code = models.CharField(max_length=6)
    creation_date = models.DateTimeField(auto_now=True)
    verification_token = models.CharField(max_length=32, null=True, blank=True)

    objects = PhoneNumberValidationManager()

    def __str__(self):
        return self.phone_number
