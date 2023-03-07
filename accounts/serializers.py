from rest_framework import serializers

from .models import PhoneNumberValidation, User
from .managers import NormalizePhoneNumber


class PhoneNumberValidationSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {"phone_number": instance.phone_number, "validation_code": instance.validation_code}

    class Meta:
        model = PhoneNumberValidation
        fields = ('phone_number',)

    def validate_phone_number(self, value):
        normalize_phone_number = NormalizePhoneNumber()
        if normalize_phone_number.validate_phone_number(value):
            return value
        raise serializers.ValidationError("Phone Number is not valid")

    def create(self, validated_data):
        phone_number = validated_data.get("phone_number")
        if PhoneNumberValidation.objects.check_phone_number_exists(phone_number):
            obj = PhoneNumberValidation.objects.get(phone_number=phone_number)
            return self.update(obj, validated_data)
        return PhoneNumberValidation.objects.create(phone_number)

    def update(self, instance, validated_data):
        return PhoneNumberValidation.objects.update_validation_code(validated_data['phone_number'])


class VerifyPhoneNumberCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumberValidation
        fields = ("phone_number", "validation_code")

    def validate(self, data):
        import datetime
        try:
            obj = PhoneNumberValidation.objects.get(phone_number=data.get("phone_number"))
        except PhoneNumberValidation.DoesNotExist:
            raise serializers.ValidationError("Phone Number is not valid")
        creation_code_date = obj.creation_date
        now_date = datetime.datetime.now(tz=creation_code_date.tzinfo)
        if now_date - obj.creation_date > datetime.timedelta(minutes=3):
            raise serializers.ValidationError("Time Limit Extended")
        elif obj.validation_code != data.get("validation_code"):
            raise serializers.ValidationError("Verification code is not correct")
        return data


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, max_length=100)
    password2 = serializers.CharField(write_only=True, max_length=100)

    class Meta:
        model = User
        fields = ('phone_number', "email", "first_name", "last_name", "gender", "age", "password1", "password2")

    def validate_phone_number(self, value):
        try:
            PhoneNumberValidation.objects.get(phone_number=value)
        except PhoneNumberValidation.DoesNotExist:
            raise serializers.ValidationError("Phone Number Should Validate First")
        return value

    def validate_age(self, value):
        if value is not None and (value < 3 or value > 80):
            raise serializers.ValidationError("user age is not allow to register")
        return value

    def validate(self, data):
        password1 = data.get("password1")
        password2 = data.get("password2")
        if password1 != password2:
            raise serializers.ValidationError({
                "password2": ["password1 and password2 are not match", ]
            })
        return data

    def create(self, validated_data):
        validated_data.pop("password1")
        password = validated_data.pop("password2")
        return User.objects.create_user(password=password, **validated_data)
