from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer

from social_network.apps.accounts.api.permissions import IsNotAuthenticated
from social_network.apps.accounts.api.serializers.login import LoginSerializer
from social_network.apps.accounts.services.login import LoginService


class LoginView(GenericAPIView):
    permission_classes = [IsNotAuthenticated]
    serializer_class = LoginSerializer

    @extend_schema(summary="Login", tags=["Accounts"], responses={status.HTTP_204_NO_CONTENT: OpenApiResponse()})
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        return LoginService.login(request, user)


class LogoutView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Serializer

    @extend_schema(summary="Log out", tags=["Accounts"], responses={status.HTTP_204_NO_CONTENT: OpenApiResponse()})
    def post(self, request):
        return LoginService.logout(request)
