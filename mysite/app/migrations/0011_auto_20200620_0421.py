# Generated by Django 3.0.7 on 2020-06-20 04:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200620_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 20, 4, 21, 36, 403491)),
        ),
        migrations.AlterField(
            model_name='memmber',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='weekly_entry',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 20, 4, 21, 36, 402753)),
        ),
    ]
