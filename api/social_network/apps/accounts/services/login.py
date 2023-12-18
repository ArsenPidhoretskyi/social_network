from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import update_last_login

from social_network.apps.accounts.models import User


class LoginService:
    @classmethod
    def login(cls, request, user):
        django_login(request, user)
        update_last_login(User, user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @classmethod
    def logout(cls, request):
        django_logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
