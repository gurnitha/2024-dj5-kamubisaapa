# Generated by Django 5.0.2 on 2024-02-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="featured_image",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="vote_ratio",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="vote_total",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]