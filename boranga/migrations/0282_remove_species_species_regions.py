# Generated by Django 3.2.25 on 2024-06-05 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0281_auto_20240605_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='species',
            name='species_regions',
        ),
    ]
