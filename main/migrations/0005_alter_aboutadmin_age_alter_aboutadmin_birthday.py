# Generated by Django 4.1.3 on 2022-12-03 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_aboutadmin_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutadmin',
            name='age',
            field=models.IntegerField(default=26, editable=False),
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='birthday',
            field=models.DateField(default=datetime.date(1996, 11, 28)),
        ),
    ]
