from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path

from social_network.apps.accounts.api.views.activity import ActivityView
from social_network.apps.accounts.api.views.login import LoginView, LogoutView
from social_network.apps.accounts.api.views.password import (
    ChangePasswordAPIView,
    ConfirmResetPasswordAPIView,
    ResetPasswordAPIView,
)
from social_network.apps.accounts.api.views.registration import RegistrationAPIView
from social_network.apps.accounts.api.views.user_profile import UserProfileAPIView


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("me/", UserProfileAPIView.as_view(), name="user-profile"),
    path("password/", ChangePasswordAPIView.as_view(), name="change-password"),
    path("password/confirm/", ConfirmResetPasswordAPIView.as_view(), name="confirm-reset-password"),
    path("password/reset/", ResetPasswordAPIView.as_view(), name="reset-password"),
    path("registration/", RegistrationAPIView.as_view(), name="registration"),
    path("activity/<int:pk>/", ActivityView.as_view(), name="registration"),
]
