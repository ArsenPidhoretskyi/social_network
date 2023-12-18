from rest_framework.serializers import ModelSerializer

from social_network.apps.accounts.models import User


class ActivitySerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "last_login",
            "last_request",
        ]
        read_only_fields = fields
