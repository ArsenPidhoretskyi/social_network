from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from social_network.apps.accounts.api.permissions import IsRequestUser
from social_network.apps.accounts.api.serializers.activity import ActivitySerializer
from social_network.apps.accounts.models import User


@extend_schema_view(
    get=extend_schema(
        summary="User activity",
        tags=["Accounts"],
    ),
)
class ActivityView(RetrieveAPIView):
    queryset = User.objects
    serializer_class = ActivitySerializer
    permission_classes = [IsAdminUser | (IsAuthenticated & IsRequestUser)]
