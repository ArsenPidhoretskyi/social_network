from rest_framework.permissions import SAFE_METHODS, BasePermission

from social_network.apps.posts.models import Post


class IsPostCreatorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj: Post):
        return request.method in SAFE_METHODS or obj.creator == request.user
