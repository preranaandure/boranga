# Generated by Django 3.2.25 on 2024-07-31 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0384_auto_20240731_1200"),
    ]

    operations = [
        migrations.AddField(
            model_name="conservationchangecode",
            name="archived",
            field=models.BooleanField(default=False),
        ),
    ]
