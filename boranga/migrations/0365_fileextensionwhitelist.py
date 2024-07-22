# Generated by Django 3.2.25 on 2024-07-22 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0364_merge_0362_auto_20240719_1506_0363_auto_20240719_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileExtensionWhitelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('model', models.CharField(choices=[], default='all', max_length=255)),
            ],
            options={
                'unique_together': {('name', 'model')},
            },
        ),
    ]
