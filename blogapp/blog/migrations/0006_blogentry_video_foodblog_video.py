# Generated by Django 4.1.3 on 2022-12-12 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_blogentry_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogentry",
            name="video",
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name="foodblog",
            name="video",
            field=models.URLField(null=True),
        ),
    ]
