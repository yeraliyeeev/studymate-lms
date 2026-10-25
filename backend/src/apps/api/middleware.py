import os

from django.http import JsonResponse
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.authentication import JWTAuthentication


class DemoReadOnlyMiddleware:
    unsafe_methods = {"POST", "PUT", "PATCH", "DELETE"}

    def __init__(self, get_response):
        self.get_response = get_response
        self.demo_email = os.getenv("DEMO_READ_ONLY_EMAIL", "").strip().lower()

    def __call__(self, request):
        if (
            self.demo_email
            and request.path.startswith("/api/")
            and request.method in self.unsafe_methods
        ):
            try:
                authentication = JWTAuthentication().authenticate(request)
            except APIException:
                authentication = None
            if authentication:
                user, _ = authentication
                if user.email.lower() == self.demo_email:
                    return JsonResponse(
                        {
                            "detail": (
                                "This public demo account is read-only. "
                                "Changes are disabled to protect the shared demo data."
                            )
                        },
                        status=403,
                    )

        return self.get_response(request)
