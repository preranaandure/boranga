# Generated by Django 3.2.25 on 2024-07-17 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0353_auto_20240715_1033"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="permittype",
            options={"ordering": ["group_type", "name"]},
        ),
    ]
