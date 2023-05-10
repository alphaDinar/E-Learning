# Generated by Django 4.2.1 on 2023-05-08 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Log', '0003_alter_manager_course_alter_teacher_course'),
        ('Scheme', '0014_slide_holder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('question_num', models.IntegerField(blank=True, default=10, null=True)),
                ('duration', models.IntegerField(help_text='Duration allowed for Quiz in minutes')),
                ('level', models.CharField(choices=[('easy', 'easy'), ('normal', 'normal'), ('difficult', 'difficult')], max_length=30)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('active', 'active'), ('completed', 'completed')], default='pending', max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Log.teacher')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scheme.scheme')),
            ],
            options={
                'verbose_name_plural': 'quizes',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('set_on', models.DateTimeField(auto_now_add=True, help_text='when question was first set')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('correct', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='when answer was first added')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.question')),
            ],
        ),
    ]