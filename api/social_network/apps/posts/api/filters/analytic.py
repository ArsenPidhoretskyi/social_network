from django_filters.rest_framework import FilterSet, filters

from social_network.apps.posts.models.post import Like


class AnalyticFilter(FilterSet):
    date_from = filters.DateFilter("created", lookup_expr="gte")
    date_to = filters.DateFilter("created", lookup_expr="lte")

    class Meta:
        model = Like
        fields = []
