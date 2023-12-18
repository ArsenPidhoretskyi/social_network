from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = "social_network.apps.accounts"

    def ready(self):
        from social_network.apps.accounts.api.extensions import SessionAuthenticationExtension  # noqa: F401
