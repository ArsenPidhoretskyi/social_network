from rest_framework.routers import DefaultRouter

from django.urls import path

from social_network.apps.posts.api.views.analytic import AnalyticView
from social_network.apps.posts.api.views.post import PostViewSet


router = DefaultRouter()
router.register("", PostViewSet)


urlpatterns = [
    path("analytic/", AnalyticView.as_view(), name="analytic"),
] + router.urls
