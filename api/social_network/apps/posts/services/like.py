from gettext import gettext

from social_network.apps.accounts.models import User
from social_network.apps.posts.exceptions import LikeAlreadyExistError, LikeDoestNotExistError
from social_network.apps.posts.models import Post


class LikeService:
    @staticmethod
    def check_like_availability(post: Post, user: User) -> None:
        if post.is_like_exist(user):
            raise LikeAlreadyExistError(gettext("You already like this post."))

    @staticmethod
    def check_unlike_availability(post: Post, user: User) -> None:
        if not post.is_like_exist(user):
            raise LikeDoestNotExistError(gettext("You doesn't like this post."))

    @staticmethod
    def like(post: Post, user: User) -> None:
        post.like(user)

    @staticmethod
    def unlike(post: Post, user: User) -> None:
        post.unlike(user)
