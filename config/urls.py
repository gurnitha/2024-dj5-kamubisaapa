# config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # projects
    path("", include("app.projects.urls")),
    # admin
    path("admin/", admin.site.urls),
]
