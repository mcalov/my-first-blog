# Generated by Django 3.0.1 on 2020-01-21 17:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='createdData',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 21, 17, 5, 30, 228918, tzinfo=utc)),
        ),
    ]
