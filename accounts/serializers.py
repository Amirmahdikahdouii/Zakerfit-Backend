# Serializers
from rest_framework import serializers

# Models
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
