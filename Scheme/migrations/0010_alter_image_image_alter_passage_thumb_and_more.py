# Generated by Django 4.2.1 on 2023-05-06 16:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Scheme', '0009_rename_image_passage_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='passage',
            name='thumb',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dvnemzw0z/image/upload/v1683386036/5064889_wpiq8e.png', max_length=255, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Video'),
        ),
    ]
