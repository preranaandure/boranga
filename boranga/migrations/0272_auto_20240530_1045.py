# Generated by Django 3.2.25 on 2024-05-30 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0271_auto_20240530_1039"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="submitterinformation",
            name="email_user",
        ),
    ]
