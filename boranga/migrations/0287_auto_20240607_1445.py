# Generated by Django 3.2.25 on 2024-06-07 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0286_auto_20240607_1234"),
    ]

    operations = [
        migrations.AddField(
            model_name="occurrencereport",
            name="submitter_information",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="occurrence_report",
                to="boranga.submitterinformation",
            ),
        ),
    ]
