from django.db import models
from django.contrib.auth.models import AbstractUser
from Course.models import Course,Grade
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    
class Teacher(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    course = models.ManyToManyField(Course,blank=True)
    password = models.CharField(max_length=100)
    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.name.username)
        user.is_teacher = True
        user.save()
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name.username

class Manager(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    course = models.ManyToManyField(Course,blank=True)
    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.name.username)
        user.is_manager = True
        user.save()
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name.username

class Student(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE) 
    # profile_pic = models.ImageField(default='student.jpg', upload_to='students')
    # profile_pic = CloudinaryField("Image" ,folder='TM/Students', resource_type='auto', default='https://res.cloudinary.com/dvnemzw0z/image/upload/v1683386036/5064889_wpiq8e.png')
    first_name = models.CharField(max_length=200) 
    last_name = models.CharField(max_length=200)
    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.name.username)
        user.is_student = True
        user.save()
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.name.username}' 
    def get_scores(self):
        return self.score_set.all()


# class LogBox(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     token = models.CharField(max_length=3000)
#     def __str__(self):
#         return f'{self.user.username} = Active' 
#     class Meta:
#         verbose_name_plural = 'Log Boxes'