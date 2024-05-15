# Generated by Django 3.2.25 on 2024-05-15 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0247_merge_0244_auto_20240514_1547_0246_auto_20240513_1413"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExternalContributorBlacklist",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("reason", models.TextField()),
                ("datetime_created", models.DateTimeField(auto_now_add=True)),
                ("datetime_updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name_plural": "External Contributor Blacklist",
            },
        ),
    ]
