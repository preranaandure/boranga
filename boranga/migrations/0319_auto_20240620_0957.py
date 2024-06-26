# Generated by Django 3.2.25 on 2024-06-20 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('boranga', '0318_merge_20240619_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occurrencegeometry',
            name='copied_from',
        ),
        migrations.RemoveField(
            model_name='occurrencereportgeometry',
            name='copied_from',
        ),
        migrations.AddField(
            model_name='buffergeometry',
            name='copied_from_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='buffergeometry',
            name='copied_from_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='occurrencegeometry',
            name='copied_from_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='occurrencegeometry',
            name='copied_from_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='occurrencereportgeometry',
            name='copied_from_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='occurrencereportgeometry',
            name='copied_from_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
