# Generated by Django 4.1.3 on 2022-12-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_aboutadmin_age_alter_aboutadmin_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='aboutadmin',
            name='degree',
            field=models.CharField(max_length=50),
        ),
    ]