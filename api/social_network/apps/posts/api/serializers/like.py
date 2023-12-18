from social_network.apps.accounts.api.mixins import RequestUserMixin
from social_network.apps.posts.api.mixins import BaseLikeSerializer


class LikeSerializer(RequestUserMixin, BaseLikeSerializer):
    def validate(self, attrs: dict) -> dict:
        attrs = super().validate(attrs)
        self.like_service.check_like_availability(self.instance, self.user)
        return attrs

    def save(self, **kwargs):
        self.like_service.like(self.instance, self.user)


class UnlikeSerializer(RequestUserMixin, BaseLikeSerializer):
    def validate(self, attrs: dict) -> dict:
        self.like_service.check_unlike_availability(self.instance, self.user)
        return attrs

    def save(self, **kwargs):
        self.like_service.unlike(self.instance, self.user)
