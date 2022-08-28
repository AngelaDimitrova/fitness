# Generated by Django 4.1 on 2022-08-27 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fitness_app', '0012_alter_question_possibleanswers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testuser',
            name='fitnessUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='testuser',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fitness_app.test'),
        ),
    ]
