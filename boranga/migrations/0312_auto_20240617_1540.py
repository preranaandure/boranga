# Generated by Django 3.2.25 on 2024-06-17 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0311_auto_20240617_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occanimalobservation',
            name='alive_adult',
        ),
        migrations.RemoveField(
            model_name='occanimalobservation',
            name='alive_juvenile',
        ),
        migrations.RemoveField(
            model_name='occanimalobservation',
            name='alive_pouch_young',
        ),
        migrations.RemoveField(
            model_name='occanimalobservation',
            name='alive_unsure',
        ),
        migrations.RemoveField(
            model_name='occanimalobservation',
            name='dead_adult',
        ),
        migrations.RemoveField(
            model_name='occanimalobservation',
            name='dead_juvenile',
        ),
        migrations.RemoveField(
            model_name='occanimalobservation',
            name='dead_pouch_young',
        ),
        migrations.RemoveField(
            model_name='occanimalobservation',
            name='dead_unsure',
        ),
        migrations.RemoveField(
            model_name='ocranimalobservation',
            name='alive_adult',
        ),
        migrations.RemoveField(
            model_name='ocranimalobservation',
            name='alive_juvenile',
        ),
        migrations.RemoveField(
            model_name='ocranimalobservation',
            name='alive_pouch_young',
        ),
        migrations.RemoveField(
            model_name='ocranimalobservation',
            name='alive_unsure',
        ),
        migrations.RemoveField(
            model_name='ocranimalobservation',
            name='dead_adult',
        ),
        migrations.RemoveField(
            model_name='ocranimalobservation',
            name='dead_juvenile',
        ),
        migrations.RemoveField(
            model_name='ocranimalobservation',
            name='dead_pouch_young',
        ),
        migrations.RemoveField(
            model_name='ocranimalobservation',
            name='dead_unsure',
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='alive_adult_female',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='alive_adult_male',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='alive_adult_unknown',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='alive_juvenile_female',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='alive_juvenile_male',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='alive_juvenile_unknown',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='alive_unsure_female',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='alive_unsure_male',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='alive_unsure_unknown',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='dead_adult_female',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='dead_adult_male',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='dead_adult_unknown',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='dead_juvenile_female',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='dead_juvenile_male',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='dead_juvenile_unknown',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='dead_unsure_female',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='dead_unsure_male',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='occanimalobservation',
            name='dead_unsure_unknown',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='alive_adult_female',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='alive_adult_male',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='alive_adult_unknown',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='alive_juvenile_female',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='alive_juvenile_male',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='alive_juvenile_unknown',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='alive_unsure_female',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='alive_unsure_male',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='alive_unsure_unknown',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='dead_adult_female',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='dead_adult_male',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='dead_adult_unknown',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='dead_juvenile_female',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='dead_juvenile_male',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='dead_juvenile_unknown',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='dead_unsure_female',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='dead_unsure_male',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ocranimalobservation',
            name='dead_unsure_unknown',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]