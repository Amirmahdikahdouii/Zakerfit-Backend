from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from rest_framework.response import Response

from accounts.serializers import PhoneNumberValidationSerializer, VerifyPhoneNumberCodeSerializer, UserSerializer

from accounts.models import User, PhoneNumberValidation


class GetVerificationCode(APIView):
    """
    ApiView to create a Phone number validation code, and start verifying users phone number
    """
    serializer_class = PhoneNumberValidationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            import kavenegar
            """
            We use kavenegar for sms verification sending
            for full document read: https://github.com/kavenegar/kavenegar-python
            """
            serializer.save()
            sms_api = kavenegar.KavenegarAPI(
                "ِYour Kavenegar Key here",
            )
            sms_api_params = {
                "sender": "10008663",
                "receptor": "0" + serializer.validated_data['phone_number'],
                "message": f"باشگاه ورزشی مایوستاتین \n کد تایید: {serializer.data.get('validation_code')}"
            }
            sms_api.sms_send(sms_api_params)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ConfirmValidationCode(APIView):
    """
    In this Endpoint, confirm validation code will do and return user if it exists.
    """
    serializer_class = VerifyPhoneNumberCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            phone_number = data.get("phone_number")
            try:
                """
                If user DoesNotExists, Return only phone_number and verification code and trying to register
                new user, but if phone number was already registered, return the user info
                """
                user_obj = User.objects.get(phone_number=phone_number)
            except User.DoesNotExist:
                from django.utils.crypto import get_random_string
                data['verify_token'] = get_random_string(length=32)
                # Add a new token for using to register a user by his phone number
                obj = PhoneNumberValidation.objects.get(phone_number=phone_number)
                obj.verification_token = data['verify_token']
                obj.save()
                return Response(data, status=200)
            data['user'] = {
                "phone_number": user_obj.phone_number,
                "email": user_obj.email,
                "first_name": user_obj.first_name,
                "last_name": user_obj.last_name,
            }
            return Response(data, status=200)
        return Response(serializer.errors, status=401)


class GetVerifyTokenAPIView(APIView):
    def post(self, request):
        phone_number = request.data.get("phone_number")
        try:
            obj = PhoneNumberValidation.objects.get(phone_number=phone_number)
            if obj.verification_token is not None:
                return Response({"token": obj.verification_token})
        except PhoneNumberValidation.DoesNotExist:
            return Response(status=404)
        return Response(status=401)


class RegisterNewUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
