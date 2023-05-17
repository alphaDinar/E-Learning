from django.db import models
from django.utils.text import slugify
from Log.models import Student
from Quiz.models import Quiz
from cloudinary.models import CloudinaryField

class StudentProfile(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # profile_pic = models.ImageField(default='student.jpg', upload_to='students')
    # profile_pic = CloudinaryField("Image" ,folder='TM/Students', resource_type='auto', default='https://res.cloudinary.com/dvnemzw0z/image/upload/v1683386036/5064889_wpiq8e.png')
    first_name = models.CharField(max_length=200) 
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.student.name}'

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