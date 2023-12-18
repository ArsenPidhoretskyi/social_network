from django.core.exceptions import ValidationError


class PostError(ValidationError):
    pass


class LikeAlreadyExistError(PostError):
    pass


class LikeDoestNotExistError(PostError):
    pass
