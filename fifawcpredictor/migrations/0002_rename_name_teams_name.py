# Generated by Django 4.1.3 on 2022-12-05 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fifawcpredictor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teams',
            old_name='Name',
            new_name='name',
        ),
    ]
