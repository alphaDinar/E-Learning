# Generated by Django 4.2.1 on 2023-06-07 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuperManager', '0002_remove_grading_grades_grading_grade_grading_max_mark_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grading',
            name='color_code',
            field=models.CharField(default='salmon', max_length=300),
        ),
    ]