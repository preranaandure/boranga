# Generated by Django 3.2.16 on 2023-02-09 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0112_taxonomy_kingdom_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxonomy',
            name='name_authority',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]