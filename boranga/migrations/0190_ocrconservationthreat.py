# Generated by Django 3.2.23 on 2024-02-06 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0189_rename_added_by_occurrencereportdocument_uploaded_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='OCRConservationThreat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threat_number', models.CharField(blank=True, default='', max_length=9)),
                ('comment', models.CharField(default='None', max_length=512)),
                ('date_observed', models.DateField(blank=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('current_impact', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='boranga.currentimpact')),
                ('occurrence_report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ocr_threats', to='boranga.occurrencereport')),
                ('potential_impact', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='boranga.potentialimpact')),
                ('potential_threat_onset', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='boranga.potentialthreatonset')),
                ('threat_agent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='boranga.threatagent')),
                ('threat_category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='boranga.threatcategory')),
            ],
        ),
    ]
