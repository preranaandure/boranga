# Generated by Django 3.2.25 on 2024-06-13 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0302_auto_20240613_1254"),
    ]

    operations = [
        migrations.AddField(
            model_name="occurrencereportdocument",
            name="can_submitter_access",
            field=models.BooleanField(default=False),
        ),
    ]
