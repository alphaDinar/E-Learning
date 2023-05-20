from django.db import models
from django.utils.text import slugify
from Log.models import Student
from Quiz.models import Quiz
from cloudinary.models import CloudinaryField

class StudentReport(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    report = models.JSONField(null=True, blank=True)
    def __str__(self):
        return f'{self.student}"s Report'

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    quiz_con = models.JSONField(blank=True,null=True) 
    quiz_ans_box = models.JSONField(blank=True,null=True) 
    mark = models.FloatField()
    choice_box = models.JSONField(blank=True,null=True) 
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=500, blank=True, null= True)
    def save(self,*args,**kwargs):
        if self.slug == None:
            self.slug = slugify(self.quiz.title) + '-' + slugify(self.student)      
        super().save(*args, **kwargs)  
    def __str__(self):
        return f'{self.student.name}   {self.quiz.title} {self.mark}'

