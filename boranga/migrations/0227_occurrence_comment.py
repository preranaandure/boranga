# Generated by Django 3.2.25 on 2024-04-22 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0226_merge_20240422_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='occurrence',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
