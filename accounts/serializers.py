from rest_framework import serializers

from .models import PhoneNumberValidation
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


class VerifyPhoneNumberCode(serializers.ModelSerializer):
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
