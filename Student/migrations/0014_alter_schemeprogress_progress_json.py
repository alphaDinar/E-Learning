# Generated by Django 4.2.1 on 2023-06-01 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0013_alter_schemeprogress_progress_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemeprogress',
            name='progress_json',
            field=models.JSONField(blank=True, default='[]', null=True),
        ),
    ]
