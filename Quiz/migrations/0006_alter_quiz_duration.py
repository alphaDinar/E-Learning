# Generated by Django 4.2.1 on 2023-05-30 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0005_quiz_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='duration',
            field=models.IntegerField(blank=True, help_text='Duration allowed for Quiz in minutes', null=True),
        ),
    ]