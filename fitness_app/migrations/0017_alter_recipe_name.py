# Generated by Django 4.1 on 2022-09-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0016_alter_question_theanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
