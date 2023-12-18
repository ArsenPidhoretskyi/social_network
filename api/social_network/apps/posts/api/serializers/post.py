from rest_framework.serializers import ModelSerializer

from social_network.apps.posts.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "pk",
            "title",
            "content",
            "likes_count",
        )
        read_only_fields = ("pk", "likes_count")
