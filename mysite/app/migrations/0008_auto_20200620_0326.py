# Generated by Django 3.0.7 on 2020-06-20 03:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_auto_20200615_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='memmber',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 20, 3, 26, 26, 122783)),
        ),
        migrations.AlterField(
            model_name='weekly_entry',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 20, 3, 26, 26, 122021)),
        ),
    ]