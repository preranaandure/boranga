# Generated by Django 3.2.12 on 2022-08-09 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0047_communityconservationattributes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='community',
            old_name='community_id',
            new_name='community_migrated_id',
        ),
    ]