# Generated by Django 3.2.25 on 2024-05-14 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0243_merge_0242_auto_20240508_1348_0242_auto_20240508_1431'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AmendmentReason',
        ),
        migrations.DeleteModel(
            name='RequiredDocument',
        ),
    ]
