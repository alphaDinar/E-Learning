# Generated by Django 4.2.1 on 2023-06-14 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0002_rename_events_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
    ]
