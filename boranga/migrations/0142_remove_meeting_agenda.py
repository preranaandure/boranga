# Generated by Django 3.2.16 on 2023-07-05 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0141_rename_porposalamendmentreason_proposalamendmentreason'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='agenda',
        ),
    ]
