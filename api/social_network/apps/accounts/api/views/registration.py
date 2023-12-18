from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView

from social_network.apps.accounts.api.serializers.registration import RegistrationSerializer
from social_network.apps.accounts.services.login import LoginService


class RegistrationAPIView(GenericAPIView):
    serializer_class = RegistrationSerializer

    @extend_schema(
        summary="Registration", tags=["Accounts"], responses={status.HTTP_204_NO_CONTENT: OpenApiResponse()}
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response = LoginService.login(request, user)
        return response
