# Generated by Django 3.0.7 on 2020-06-24 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20200624_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 24, 15, 34, 48, 580025)),
        ),
        migrations.AlterField(
            model_name='loan_interest',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 6, 24, 15, 34, 48, 580664)),
        ),
        migrations.AlterField(
            model_name='memmber',
            name='mobile_no',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='weekly_entry',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 24, 15, 34, 48, 579286)),
        ),
    ]
