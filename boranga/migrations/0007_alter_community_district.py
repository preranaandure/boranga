# Generated by Django 3.2.12 on 2022-05-31 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0006_auto_20220531_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='district',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='boranga.district'),
        ),
    ]
