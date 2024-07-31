# Generated by Django 3.2.25 on 2024-07-31 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0386_auto_20240731_1348"),
    ]

    operations = [
        migrations.AddField(
            model_name="commonwealthconservationlist",
            name="archived",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="walegislativelist",
            name="archived",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="waprioritylist",
            name="archived",
            field=models.BooleanField(default=False),
        ),
    ]
