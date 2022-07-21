# Generated by Django 3.2.12 on 2022-07-07 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0030_auto_20220707_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conservationstatus',
            name='change_code',
        ),
        migrations.RemoveField(
            model_name='conservationstatus',
            name='conservation_category',
        ),
        migrations.RemoveField(
            model_name='conservationstatus',
            name='conservation_criteria',
        ),
        migrations.RemoveField(
            model_name='conservationstatus',
            name='conservation_list',
        ),
        migrations.DeleteModel(
            name='ConservationCategory',
        ),
        migrations.DeleteModel(
            name='ConservationChangeCode',
        ),
        migrations.DeleteModel(
            name='ConservationCriteria',
        ),
        migrations.DeleteModel(
            name='ConservationList',
        ),
        migrations.DeleteModel(
            name='ConservationStatus',
        ),
    ]
