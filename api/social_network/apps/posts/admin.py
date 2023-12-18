from django.contrib import admin

from social_network.apps.posts.models import Like, Post


class LikeInline(admin.TabularInline):
    model = Like
    fields = ("user", "created")
    readonly_fields = ("created",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "content",
    )
    list_display = ("pk", "title", "likes_count")
    search_fields = ("title",)
    inlines = (LikeInline,)
