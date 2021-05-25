# Generated by Django 3.0.7 on 2020-06-21 08:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200621_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 8, 30, 25, 1524)),
        ),
        migrations.AlterField(
            model_name='loan_interest',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 8, 30, 25, 2155)),
        ),
        migrations.AlterField(
            model_name='weekly_entry',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 8, 30, 25, 808)),
        ),
    ]