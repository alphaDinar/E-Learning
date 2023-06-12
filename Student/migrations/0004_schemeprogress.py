# Generated by Django 4.2.1 on 2023-05-31 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0002_manager_password'),
        ('Course', '0001_initial'),
        ('Scheme', '0002_recentscheme'),
        ('Student', '0003_delete_quizsession'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchemeProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress_json', models.JSONField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.course')),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scheme.scheme')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Log.student')),
            ],
        ),
    ]