# Generated by Django 4.2.1 on 2023-06-12 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0022_schemeprogress_ratings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schemeprogress',
            old_name='ratings',
            new_name='rating',
        ),
    ]
