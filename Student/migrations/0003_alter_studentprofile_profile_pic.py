# Generated by Django 4.2.1 on 2023-05-17 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_studentprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='profile_pic',
            field=models.ImageField(default='student.jpg', upload_to='students'),
        ),
    ]