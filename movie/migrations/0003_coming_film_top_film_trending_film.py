# Generated by Django 4.1.4 on 2022-12-08 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0002_tablemovie_gambar"),
    ]

    operations = [
        migrations.CreateModel(
            name="coming_film",
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
                ("title", models.CharField(max_length=225)),
                ("overview", models.TextField()),
                ("adult", models.CharField(max_length=225)),
                ("languages", models.CharField(max_length=200)),
                ("release", models.CharField(max_length=200)),
                ("poster", models.CharField(max_length=200)),
                ("vote", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="top_film",
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
                ("title", models.CharField(max_length=225)),
                ("overview", models.TextField()),
                ("adult", models.CharField(max_length=225)),
                ("languages", models.CharField(max_length=200)),
                ("release", models.CharField(max_length=200)),
                ("poster", models.CharField(max_length=200)),
                ("vote", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Trending_film",
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
                ("title", models.CharField(max_length=225)),
                ("overview", models.TextField()),
                ("adult", models.CharField(max_length=225)),
                ("languages", models.CharField(max_length=200)),
                ("release", models.CharField(max_length=200)),
                ("poster", models.CharField(max_length=200)),
                ("vote", models.CharField(max_length=200)),
            ],
        ),
    ]
