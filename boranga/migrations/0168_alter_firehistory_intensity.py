# Generated by Django 3.2.20 on 2023-09-13 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0167_merge_20230913_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firehistory',
            name='intensity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='boranga.intensity'),
        ),
    ]
