# Generated by Django 5.0.8 on 2024-08-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0404_landform_archived_alter_communitydocument__file_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="proposalamendmentreason",
            name="archived",
            field=models.BooleanField(default=False),
        ),
    ]
