# Generated by Django 4.2.1 on 2023-05-10 17:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scheme', '0017_alter_image_image_alter_passage_thumb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='Scheme_images'),
        ),
        migrations.AlterField(
            model_name='passage',
            name='thumb',
            field=models.ImageField(blank=True, default='https://res.cloudinary.com/dvnemzw0z/image/upload/v1683386036/5064889_wpiq8e.png', null=True, upload_to='Scheme_images'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(default='vid.jpg', upload_to='TM/Scheme_video', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]
