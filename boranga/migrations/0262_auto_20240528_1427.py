# Generated by Django 3.2.25 on 2024-05-28 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0261_merge_20240524_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitytaxonomy',
            name='community_migrated_id',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='communitytaxonomy',
            name='community_name',
            field=models.CharField(blank=True, max_length=512, null=True, unique=True),
        ),
    ]