from typing import Callable

from django.http import HttpRequest, HttpResponse
from django.utils import timezone


class LastRequestMiddleware:
    def __init__(self, get_response: Callable) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        response = self.get_response(request)

        if request.user.is_authenticated:
            request.user.last_request = timezone.now()
            request.user.save(update_fields=["last_request"])

        return response
