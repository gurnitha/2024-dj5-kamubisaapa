# Generated by Django 5.0.2 on 2024-02-27 12:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_review"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("name", models.CharField(max_length=200)),
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
