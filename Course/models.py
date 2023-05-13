from django.db import models
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Subject(models.Model):
    name = models.CharField(max_length=300)
    abb = models.CharField(max_length=100, blank=True,null=True)
    slug = models.SlugField(blank=True,null=True)
    def save(self, *args, **kwargs):
        if self.slug is None:
             self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.name}"
    # def get_schemes(self):
    #     return self.scheme_set.all()

class Grade(models.Model):
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=100)
    # courses = models.ManyToManyField(Subject)
    def __str__(self):
        return f'{self.name}'
    def get_courses(self):
        return self.course_set.all()

class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE) 
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True,null=True)
    def save(self, *args, **kwargs):
        if self.slug is None:
             self.slug = slugify(self.subject.abb) + slugify(self.grade.code)
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.subject.abb} {self.grade.code}'   
    def get_schemes(self):
        return self.scheme_set.all()  
    
# class CourseReview(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     review = models.TextField(max_length=3000)
#     ratings = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
#     date_posted = models.DateTimeField(auto_now_add=True)
#     slug = models.SlugField()
#     def __str__(self):
#         return self.slug[:30]