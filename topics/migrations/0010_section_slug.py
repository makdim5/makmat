# Generated by Django 3.2.9 on 2021-11-20 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0009_auto_20211120_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL'),
        ),
    ]