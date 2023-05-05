# Generated by Django 4.2.1 on 2023-05-05 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0008_grade_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='courses',
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.grade')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.subject')),
            ],
        ),
    ]
