# Generated by Django 4.2.1 on 2023-06-07 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scheme', '0004_alter_passage_thumb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=3000)),
            ],
        ),
    ]