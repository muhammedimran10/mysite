# Generated by Django 3.0.7 on 2020-06-13 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200613_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='remarks',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
