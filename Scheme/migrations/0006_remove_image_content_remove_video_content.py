# Generated by Django 4.2.1 on 2023-05-05 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Scheme', '0005_scheme_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='content',
        ),
        migrations.RemoveField(
            model_name='video',
            name='content',
        ),
    ]