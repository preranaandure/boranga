# Generated by Django 3.2.20 on 2023-07-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0145_auto_20230712_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='comment',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]