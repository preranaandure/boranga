# Generated by Django 3.2.25 on 2024-07-04 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0332_merge_0331_auto_20240702_1430_0331_auto_20240702_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='OccurrenceTenureVesting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vesting', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Occurrence Tenure Vesting',
                'verbose_name_plural': 'Occurrence Tenure Vestings',
            },
        ),
    ]
