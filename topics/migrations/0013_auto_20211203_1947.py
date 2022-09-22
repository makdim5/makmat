# Generated by Django 3.2.9 on 2021-12-03 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topics', '0012_taskcomplition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcomplition',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='topics.task'),
        ),
        migrations.AlterField(
            model_name='taskcomplition',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]