# Generated by Django 3.2.25 on 2024-06-06 03:46

import boranga.components.conservation_status.models
import boranga.components.meetings.models
import boranga.components.occurrence.models
import boranga.components.species_and_communities.models
import boranga.components.users.models
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0284_auto_20240606_1001"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conservationstatusdocument",
            name="can_submitter_access",
            field=models.BooleanField(default=False),
        ),
    ]