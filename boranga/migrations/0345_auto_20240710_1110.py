# Generated by Django 3.2.25 on 2024-07-10 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0344_merge_0339_auto_20240708_1344_0343_auto_20240708_1509"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="occanimalobservation",
            name="total_count",
        ),
        migrations.RemoveField(
            model_name="ocranimalobservation",
            name="total_count",
        ),
    ]
