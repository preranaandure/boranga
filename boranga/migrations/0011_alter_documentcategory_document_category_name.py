# Generated by Django 3.2.12 on 2022-06-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0010_alter_documentsubcategory_document_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentcategory',
            name='document_category_name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]