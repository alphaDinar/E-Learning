# Generated by Django 4.2.1 on 2023-06-14 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuperManager', '0006_event_end_date_event_slug_event_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, null=True),
        ),
    ]
