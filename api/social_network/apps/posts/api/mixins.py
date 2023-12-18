from social_network.apps.commons.api.serializers import CoreSerializer
from social_network.apps.posts.services.like import LikeService


class BaseLikeSerializer(CoreSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.like_service = LikeService()

    def validate(self, attrs: dict) -> dict:
        if self.instance is None:
            raise NotImplementedError("Use LikeSerializerMixin only with instance")

        return attrs
