# Generated by Django 3.2.25 on 2024-07-25 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0370_auto_20240724_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="sampletype",
            options={"ordering": ["group_type", "name"]},
        ),
        migrations.RemoveField(
            model_name="speciesconservationattributes",
            name="response_to_disturbance",
        ),
    ]