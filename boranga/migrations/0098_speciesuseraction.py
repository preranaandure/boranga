# Generated by Django 3.2.16 on 2023-01-16 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0097_communityuseraction'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeciesUserAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who', models.IntegerField()),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('what', models.TextField()),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_logs', to='boranga.species')),
            ],
            options={
                'ordering': ('-when',),
            },
        ),
    ]