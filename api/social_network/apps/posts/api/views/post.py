from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from social_network.apps.posts.api.permissions import IsPostCreatorOrReadOnly
from social_network.apps.posts.api.serializers.like import LikeSerializer, UnlikeSerializer
from social_network.apps.posts.api.serializers.post import PostSerializer
from social_network.apps.posts.models import Post


POSTS_TAGS = ["Posts"]


@extend_schema_view(
    list=extend_schema(
        summary="Posts",
        tags=POSTS_TAGS,
    ),
    retrieve=extend_schema(
        summary="Read post",
        tags=POSTS_TAGS,
    ),
    create=extend_schema(
        summary="Create post",
        tags=POSTS_TAGS,
    ),
    update=extend_schema(
        summary="Update post",
        tags=POSTS_TAGS,
    ),
    partial_update=extend_schema(
        summary="Update post",
        tags=POSTS_TAGS,
    ),
    destroy=extend_schema(
        summary="Delete post",
        tags=POSTS_TAGS,
    ),
)
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly & IsPostCreatorOrReadOnly]
    serializer_class = PostSerializer
    serializer_classes = {
        "like": LikeSerializer,
        "unlike": UnlikeSerializer,
    }

    def get_permissions(self):
        if self.action in ["like", "unlike"]:
            return [IsAuthenticatedOrReadOnly()]
        return super().get_permissions()

    def perform_create(self, serializer):
        if self.action == "create":
            serializer.save(creator=self.request.user)
        return super().perform_create(serializer)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, super().get_serializer_class())

    def _like_unlike(self, request) -> Response:
        serializer = self.get_serializer(self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(summary="Like", tags=POSTS_TAGS, responses={status.HTTP_204_NO_CONTENT: OpenApiResponse()})
    @action(methods=["POST"], detail=True)
    def like(self, request, *args, **kwargs):
        return self._like_unlike(request)

    @extend_schema(summary="Unlike", tags=POSTS_TAGS, responses={status.HTTP_204_NO_CONTENT: OpenApiResponse()})
    @action(methods=["POST"], detail=True)
    def unlike(self, request, *args, **kwargs):
        return self._like_unlike(request)
