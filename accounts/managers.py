from django.contrib.auth.models import BaseUserManager
from django.db import models


class NormalizePhoneNumber:
    def normalize_phone_number(self, phone_number):
        """
        We Use phonenumbers python package for normalize phone numbers.
        you can see the docs here: https://github.com/daviddrysdale/python-phonenumbers
        """
        import phonenumbers
        phone_number = phonenumbers.parse(phone_number, "IR")
        if phonenumbers.is_valid_number(phone_number):
            return phone_number.national_number
        raise ValueError("Phone number is not valid")

    def validate_phone_number(self, phone_number):
        import phonenumbers
        try:
            phone_number = phonenumbers.parse(phone_number, "IR")
        except AttributeError:
            return False
        except phonenumbers.NumberParseException:
            return False
        if phonenumbers.is_valid_number(phone_number):
            return True
        return False


class CustomUserManager(NormalizePhoneNumber, BaseUserManager):
    def create_user(self, phone_number, first_name, last_name, password=None, email=None, **options):
        if password is None:
            raise ValueError("Password is required")
        obj = self.model(
            phone_number=self.normalize_phone_number(phone_number),
            first_name=first_name,
            last_name=last_name,
            **options
        )
        if email is not None:
            obj.email = self.normalize_email(email)
        obj.set_password(password)
        obj.save()
        return obj

    def create_superuser(self, phone_number, first_name, last_name, password=None, **options):
        obj = self.create_user(phone_number, first_name, last_name, password, **options)
        obj.is_admin = True
        obj.save()
        return obj

    def check_phone_number_exists(self, phone_number):
        return self.filter(phone_number=phone_number).exists()


class PhoneNumberValidationManager(NormalizePhoneNumber, models.Manager):

    def generate_validation_code(self):
        import random
        return random.randint(111111, 999999)

    def create(self, phone_number, validation_code=None):
        phone_number = self.normalize_phone_number(phone_number)
        if validation_code is None:
            validation_code = self.generate_validation_code()
        if self.filter(phone_number=phone_number).exists():
            raise ValueError("Phone Number is Already Exists. Please Update Phone Number Validation Code")
        obj = self.model(phone_number=phone_number, validation_code=validation_code)
        obj.save()
        return obj

    def update_validation_code(self, phone_number, validation_code=None):
        try:
            obj = self.get(phone_number=phone_number)
            if validation_code is None:
                validation_code = self.generate_validation_code()
            obj.validation_code = validation_code
            obj.save()
            return obj
        except self.model.DoesNotExist:
            raise ValueError("Phone Number Not Exists, Please create one!")

    def check_phone_number_exists(self, phone_number):
        return self.filter(phone_number=self.normalize_phone_number(phone_number)).exists()
