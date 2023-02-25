from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
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
