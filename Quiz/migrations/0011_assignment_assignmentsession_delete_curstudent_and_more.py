# Generated by Django 4.2.1 on 2023-06-02 11:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Scheme', '0004_alter_passage_thumb'),
        ('Quiz', '0010_alter_quiz_duration_alter_quizsession_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('question_num', models.IntegerField(blank=True, default=10, null=True)),
                ('deadline', models.DateTimeField(default=django.utils.timezone.now)),
                ('con', models.JSONField(blank=True, null=True)),
                ('marking_scheme', models.JSONField(blank=True, null=True)),
                ('progress', models.CharField(choices=[('pending', 'pending'), ('active', 'active'), ('completed', 'completed')], default='pending', max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('locked', 'locked'), ('unlocked', 'unlocked')], default='locked', max_length=50)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scheme.scheme')),
            ],
            options={
                'verbose_name_plural': 'quizes',
            },
        ),
        migrations.CreateModel(
            name='AssignmentSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(blank=True, max_length=100, null=True)),
                ('assignment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Quiz.assignment')),
            ],
        ),
        migrations.DeleteModel(
            name='CurStudent',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='status',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='type',
        ),
    ]
