# Generated by Django 4.2.1 on 2023-05-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0004_remove_quiz_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='progress',
            field=models.CharField(choices=[('pending', 'pending'), ('active', 'active'), ('completed', 'completed')], default='pending', max_length=20),
        ),
    ]
