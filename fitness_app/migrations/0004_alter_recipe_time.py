# Generated by Django 4.1 on 2022-08-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0003_recipe_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.CharField(max_length=10),
        ),
    ]
