# Generated by Django 3.2.25 on 2024-07-08 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0338_merge_20240705_1005"),
    ]

    operations = [
        migrations.AddField(
            model_name="meetingroom",
            name="archived",
            field=models.BooleanField(default=False),
        ),
    ]
