# Generated by Django 3.0.7 on 2020-06-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekly_entry',
            name='remarks',
            field=models.CharField(default='', max_length=50),
        ),
    ]
