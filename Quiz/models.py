
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from Log.models import User, Teacher
from Course.models import Course
from Scheme.models import Scheme

Q_level = (
    ('easy', 'easy'),
    ('normal', 'normal'),
    ('difficult', 'difficult'),
)
Q_status = (
    ('pending','pending'),
    ('active','active'),
    ('completed','completed')
)

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    topic = models.ForeignKey(Scheme, on_delete=models.CASCADE)
    question_num = models.IntegerField(blank=True, null=True, default=10)
    duration = models.IntegerField(
        help_text='Duration allowed for Quiz in minutes')
    level = models.CharField(max_length=30, choices=Q_level)
    con = models.JSONField(blank=True,null=True)
    marking_scheme = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=Q_status, default='pending')
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.slug == None:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'quizes'

class Score(models.Model):
    quiz_title = models.CharField(max_length=300)
    quiz_con = models.JSONField(blank=True,null=True) 
    quiz_ans_box = models.JSONField(blank=True,null=True) 
    mark = models.FloatField()
    choice_box = models.JSONField(blank=True,null=True) 
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.quiz_title} {self.mark}'

# class MarkingScheme(models.Model):
#     answers = models.JSONField()
#     quiz = models.OneToOneField(Quiz, on_delete=models.CASCADE)
#     def str__(self):
#         return f"{self.quiz.name}'s marking scheme"


# class Score(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     user_choice = models.JSONField()
#     score = models.FloatField()
#     time_taken = models.IntegerField(default=10)
#     time_completed = models.DateTimeField(default=timezone.now)
#     def __str__(self):
#         return f'{self.quiz} score'