from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def root_status(_request):
    return JsonResponse(
        {"service": "personal-portfolio-backend", "docs": "/api/health/"}
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("main_app.api_urls")),
    path("", root_status, name="root-status"),
]
