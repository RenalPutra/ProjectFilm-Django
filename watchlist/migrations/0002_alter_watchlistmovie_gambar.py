# Generated by Django 4.1.3 on 2022-11-16 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="watchlistmovie",
            name="gambar",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
