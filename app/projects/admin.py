# app/projects/models.py

# Django modules
from django.contrib import admin

# Loclas
from app.projects.models import Project, Review, Tag

# Register your models here.

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)