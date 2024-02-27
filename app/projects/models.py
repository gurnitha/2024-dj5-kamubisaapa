# app/projects/models.py

# Django and third parties modules
from django.db import models
import uuid # to overide the default id in the table

# Locals

# Create your models here.

# MODELS:Project
class Project(models.Model):
    title = models.CharField(
        max_length=200)
    description = models.TextField(
        null=True, 
        blank=True)
    featured_image = models.ImageField(
        null=True, 
        blank=True, 
        default="default.jpg")
    demo_link = models.CharField(
        max_length=2000, 
        null=True, 
        blank=True)
    source_link = models.CharField(
        max_length=2000, 
        null=True, 
        blank=True)
    vote_total = models.IntegerField(
        default=0, 
        null=True, 
        blank=True)
    vote_ratio = models.IntegerField(
        default=0, 
        null=True, 
        blank=True)
    created = models.DateTimeField(
                auto_now_add=True)
    ''' Using uuid means that to overide 
        the default id in the table
        and use it as primary key and not editable'''
    id = models.UUIDField(
                default=uuid.uuid4, unique=True,
                primary_key=True, editable=False)

    def __str__(self):
        return self.title