# Generated by Django 3.2.25 on 2024-07-31 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0385_auto_20240731_1216"),
    ]

    operations = [
        migrations.AddField(
            model_name="submittercategory",
            name="archived",
            field=models.BooleanField(default=False),
        ),
    ]
