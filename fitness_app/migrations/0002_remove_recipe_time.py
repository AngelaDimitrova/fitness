# Generated by Django 4.1 on 2022-08-07 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='time',
        ),
    ]
