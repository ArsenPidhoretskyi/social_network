from __future__ import annotations

from django.db import models
from django.utils.translation import gettext_lazy as _

from social_network.apps.accounts.models import User
from social_network.apps.commons.models import CoreModel


class Post(CoreModel):
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.CharField(max_length=255)
    content = models.TextField()

    likes: models.ManyToManyField[User, Like] = models.ManyToManyField(
        User, related_name="liked_posts", through="Like"
    )

    @property
    def likes_count(self) -> int:
        return self.likes.count()

    def is_like_exist(self, user: User) -> bool:
        return self.likes.filter(id=user.pk).exists()

    def like(self, user: User) -> None:
        self.likes.add(user)

    def unlike(self, user: User) -> None:
        self.likes.remove(user)


class Like(models.Model):
    created = models.DateField(auto_now_add=True, db_index=True, verbose_name=_("created"))

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="likes_through",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="likes_through",
    )

    objects = models.Manager()

    def __str__(self) -> str:
        return f"Liked post {self.post} by {self.user}"
