# Generated by Django 4.1.4 on 2022-12-23 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0005_searching_film"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="searching_film",
            name="idcom",
        ),
        migrations.AddField(
            model_name="searching_film",
            name="idsearch",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
