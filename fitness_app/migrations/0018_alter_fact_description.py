# Generated by Django 4.1 on 2022-09-04 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0017_alter_recipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fact',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
