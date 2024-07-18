# Generated by Django 3.2.25 on 2024-07-18 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0358_auto_20240718_1018"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="systememailgroup",
            name="label",
        ),
        migrations.AlterField(
            model_name="systememailgroup",
            name="area",
            field=models.CharField(
                blank=True,
                choices=[
                    ("conservation_status", "Conservation Status"),
                    ("occurrence", "Occurrence"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
