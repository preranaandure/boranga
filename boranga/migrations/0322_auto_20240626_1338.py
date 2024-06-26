# Generated by Django 3.2.25 on 2024-06-26 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0321_merge_0320_auto_20240620_1103_0320_auto_20240621_1002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='occurrencereport',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='community',
            name='processing_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('discarded', 'Discarded'), ('active', 'Active'), ('historical', 'Historical'), ('to_be_split', 'To Be Split'), ('to_be_combined', 'To Be Combined'), ('to_be_renamed', 'To Be Renamed')], default='draft', max_length=30, verbose_name='Processing Status'),
        ),
        migrations.AlterField(
            model_name='species',
            name='processing_status',
            field=models.CharField(blank=True, choices=[('draft', 'Draft'), ('discarded', 'Discarded'), ('active', 'Active'), ('historical', 'Historical'), ('to_be_split', 'To Be Split'), ('to_be_combined', 'To Be Combined'), ('to_be_renamed', 'To Be Renamed')], default='draft', max_length=30, null=True, verbose_name='Processing Status'),
        ),
        migrations.AlterUniqueTogether(
            name='occcontactdetail',
            unique_together={('contact_name', 'occurrence', 'visible')},
        ),
        migrations.AlterUniqueTogether(
            name='ocrobserverdetail',
            unique_together={('observer_name', 'occurrence_report', 'visible')},
        ),
    ]
