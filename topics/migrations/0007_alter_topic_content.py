# Generated by Django 3.2.9 on 2021-11-19 21:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0006_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]