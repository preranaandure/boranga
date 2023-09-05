# Generated by Django 3.2.20 on 2023-08-09 07:48

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0157_drainage_firehistory_habitatcomposition_habitatcondition_intensity_landform_occurrencereport_rocktyp'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitatcomposition',
            name='land_form',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[], max_length=250, null=True),
        ),
    ]
