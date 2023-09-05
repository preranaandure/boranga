# Generated by Django 3.2.20 on 2023-07-12 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0146_community_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitydistribution',
            name='number_of_iucn_subpopulations',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='speciesdistribution',
            name='number_of_iucn_subpopulations',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]