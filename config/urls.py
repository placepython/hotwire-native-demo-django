"""
URL configuration for HotwireDemo project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("hotwiredemo.urls")),
    path("users/", include("django.contrib.auth.urls")),
    path("__debug__/", include("debug_toolbar.urls"))
]
