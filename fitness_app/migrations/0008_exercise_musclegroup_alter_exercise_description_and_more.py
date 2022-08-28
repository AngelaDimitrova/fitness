# Generated by Django 4.1 on 2022-08-21 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0007_exercise_alter_musclegroup_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='muscleGroup',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='fitness_app.musclegroup'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='explanatoryImage',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
