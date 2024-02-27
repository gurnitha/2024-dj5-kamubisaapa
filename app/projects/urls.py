# app/projects/views.py

# Django and third parties modules
from django.urls import path

# Locals
from app.projects import views 

urlpatterns = [
    path("", views.hallo_world),
]
