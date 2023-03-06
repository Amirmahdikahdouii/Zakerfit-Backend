from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("get-verification-code/", views.GetVerificationCode.as_view(), name='get_verification_code'),
]
