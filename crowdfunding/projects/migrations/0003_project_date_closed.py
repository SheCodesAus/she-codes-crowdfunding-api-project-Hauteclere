# Generated by Django 4.0.2 on 2023-01-20 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_closed',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 12, 57, 0, 634129)),
            preserve_default=False,
        ),
    ]