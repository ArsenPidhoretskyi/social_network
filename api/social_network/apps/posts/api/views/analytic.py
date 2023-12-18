from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import ListAPIView

from django.db.models import Count, QuerySet

from social_network.apps.posts.api.filters.analytic import AnalyticFilter
from social_network.apps.posts.api.serializers.analytic import AnalyticSerializer
from social_network.apps.posts.models import Like


@extend_schema_view(
    get=extend_schema(
        summary="Likes analytic",
        tags=["Posts"],
    ),
)
class AnalyticView(ListAPIView):
    queryset = Like.objects
    filterset_class = AnalyticFilter
    serializer_class = AnalyticSerializer

    def filter_queryset(self, queryset: QuerySet) -> QuerySet:
        queryset = super().filter_queryset(queryset)
        return (
            queryset.values("created")
            .annotate(
                count=Count("id"),
            )
            .order_by("created")
        )
