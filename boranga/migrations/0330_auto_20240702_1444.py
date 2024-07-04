# Generated by Django 3.2.25 on 2024-07-02 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boranga", "0329_merge_0326_auto_20240701_1035_0328_auto_20240701_0931"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conservationstatus",
            name="approval_level",
            field=models.CharField(
                choices=[("immediate", "Immediate"), ("minister", "Ministerial")],
                max_length=20,
                null=True,
            ),
        ),
    ]