from django.urls import path

from accounts import views

app_name = "accounts"
urlpatterns = [
    path("get-verification-code/", views.GetVerificationCode.as_view(), name='get_verification_code'),
    path("confirm-verification-code/", views.ConfirmValidationCode.as_view(), name='confirm_verification_code'),
    path("register/", views.RegisterNewUserAPIView.as_view(), name="register_new_user"),
]
