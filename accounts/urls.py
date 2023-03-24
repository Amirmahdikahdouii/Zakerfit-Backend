from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts import views

app_name = "accounts"
urlpatterns = [
    path("get-verification-code/", views.GetVerificationCode.as_view(), name='get_verification_code'),
    path("confirm-verification-code/", views.ConfirmValidationCode.as_view(), name='confirm_verification_code'),
    path("get-verify-token/", views.GetVerifyTokenAPIView.as_view(), name='get_verify_code'),
    path("register/", views.RegisterNewUserAPIView.as_view(), name="register_new_user"),
    path("token/", TokenObtainPairView.as_view(), name="JWT_token_obtain_pair_view"),
    path("token/refresh/", TokenRefreshView.as_view(), name="JWT_token_refresh_view"),
]
