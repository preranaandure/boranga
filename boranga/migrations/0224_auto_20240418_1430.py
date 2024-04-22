# Generated by Django 3.2.25 on 2024-04-18 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0223_merge_20240417_1423"),
    ]

    operations = [
        migrations.AddField(
            model_name="district",
            name="code",
            field=models.CharField(max_length=3, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="district",
            name="name",
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name="region",
            name="name",
            field=models.CharField(default=None, max_length=64, unique=True),
        ),
    ]
