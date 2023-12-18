from rest_framework import serializers

from social_network.apps.accounts.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")
