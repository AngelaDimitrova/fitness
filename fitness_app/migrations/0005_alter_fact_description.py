# Generated by Django 4.1 on 2022-08-15 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0004_alter_recipe_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fact',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
