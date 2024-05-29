# Generated by Django 3.2.25 on 2024-05-29 05:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0264_auto_20240529_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geoserverurl',
            name='requires_basic_auth',
        ),
        migrations.AddField(
            model_name='tilelayer',
            name='max_zoom',
            field=models.PositiveIntegerField(default=21, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(21)]),
        ),
        migrations.AddField(
            model_name='tilelayer',
            name='min_zoom',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(21)]),
        ),
    ]
