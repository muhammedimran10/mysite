# Generated by Django 3.0.7 on 2020-06-20 04:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200620_0326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memmber',
            name='account_no',
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 20, 4, 16, 59, 445102)),
        ),
        migrations.AlterField(
            model_name='weekly_entry',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 20, 4, 16, 59, 444372)),
        ),
    ]
