# Generated by Django 4.2.1 on 2023-06-14 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0001_initial'),
        ('SuperManager', '0004_alter_grading_max_mark_alter_grading_min_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('grade', models.ManyToManyField(to='Course.grade')),
            ],
        ),
    ]