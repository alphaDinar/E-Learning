# Generated by Django 4.2.1 on 2023-05-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0004_rename_slug_course_abbreviation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='abbreviation',
            new_name='slug',
        ),
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]