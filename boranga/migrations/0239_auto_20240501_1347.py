# Generated by Django 3.2.25 on 2024-05-01 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0238_merge_20240429_1615"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="occurrencereportamendmentrequest",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="occurrencereportproposalrequest",
            options={"ordering": ["id"]},
        ),
        migrations.AlterField(
            model_name="occurrencereportapprovaldetails",
            name="occurrence",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="boranga.occurrence",
            ),
        ),
    ]
