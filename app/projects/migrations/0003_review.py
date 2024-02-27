# Generated by Django 5.0.2 on 2024-02-27 10:04

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_project_featured_image_project_vote_ratio_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                ("body", models.TextField(blank=True, null=True)),
                (
                    "value",
                    models.CharField(
                        choices=[("up", "Up Vote"), ("down", "Down Vote")],
                        max_length=200,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
    ]
