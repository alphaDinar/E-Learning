# Generated by Django 4.2.1 on 2023-05-05 11:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=300)),
                ('grade', models.CharField(max_length=300)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=3000)),
                ('ratings', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.course')),
            ],
        ),
    ]
