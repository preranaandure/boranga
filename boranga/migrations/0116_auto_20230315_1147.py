# Generated by Django 3.2.16 on 2023-03-15 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0115_species_parent_species'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxonomy',
            name='kingdom_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taxons', to='boranga.kingdom'),
        ),
        migrations.CreateModel(
            name='TaxonomyRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kingdom_id', models.IntegerField(blank=True, null=True)),
                ('taxon_rank_id', models.IntegerField(blank=True, null=True)),
                ('rank_name', models.CharField(blank=True, max_length=512, null=True)),
                ('kingdom_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ranks', to='boranga.kingdom')),
            ],
        ),
    ]
