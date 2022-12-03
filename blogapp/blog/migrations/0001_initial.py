# Generated by Django 4.1.3 on 2022-12-03 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("image", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("entry", models.TextField()),
                ("isActive", models.BooleanField()),
                ("isHome", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="FoodBlog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("image", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("entry", models.TextField()),
                ("isActive", models.BooleanField()),
                ("isHome", models.BooleanField()),
            ],
        ),
    ]
