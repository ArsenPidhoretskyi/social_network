from pathlib import Path

from .environment import env


BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = env.bool("SOCIAL_NETWORK_DEBUG", default=False)

INTERNAL_IPS = env.list("SOCIAL_NETWORK_INTERNAL_IPS", default=[])

ALLOWED_HOSTS = env.list("SOCIAL_NETWORK_ALLOWED_HOSTS", default=[])

SECRET_KEY = env.str("SOCIAL_NETWORK_SECRET_KEY")


DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


THIRD_PARTY_APPS = [
    "django_extensions",
    "django_filters",
    "drf_spectacular",
    "rest_framework",
    "rest_framework_simplejwt",
]

FIRST_PARTY_APPS = [
    "social_network.apps.commons",
    "social_network.apps.accounts",
    "social_network.apps.posts",
]

INSTALLED_APPS = [
    *DJANGO_APPS,
    *THIRD_PARTY_APPS,
    *FIRST_PARTY_APPS,
    *env.list("SOCIAL_NETWORK_DEV_INSTALLED_APPS", default=[]),
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_network.apps.accounts.api.middlewares.LastRequestMiddleware",
] + env.list("SOCIAL_NETWORK_DEV_MIDDLEWARE", default=[])

ROOT_URLCONF = "social_network.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "social_network.wsgi.application"

DATABASES = {
    "default": env.db("SOCIAL_NETWORK_DATABASE_URL"),
}

AUTH_USER_MODEL = "accounts.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = env.str("SOCIAL_NETWORK_TIME_ZONE", default="UTC")

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [BASE_DIR / ".." / ".." / "api" / "locale"]


STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"


APPEND_SLASH = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
