# Generated by Django 4.2.1 on 2023-05-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0005_rename_abbreviation_course_slug_course_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='code',
        ),
        migrations.AddField(
            model_name='course',
            name='abb',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
