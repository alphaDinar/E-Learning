from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User,Student,Teacher
from Course.models import Course,Grade
from Student.models import StudentProfile

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    if user.is_student:
                        return redirect('student_dash')
                    else:
                        return redirect('courses_page')
            else:
                messages.error(request, 'Wrong password')
        else:
            messages.error(request, 'Username doesn"t exist')
    return render(request, 'index.html')

def logout_page(request):
    logout(request)
    return redirect('homepage')


def portal(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    if user.is_superuser:
                        return redirect('student_portal')
                    else:
                        messages.error(request, 'You don"t have authorized access')
            else:
                messages.error(request, 'Wrong password')
        else:
            messages.error(request, 'Username doesn"t exist')
    return render(request, 'portal.html')

def student_portal(request):
    if not request.user.is_superuser:
        return redirect('portal')
    grades = Grade.objects.all()
    if request.method == 'POST':
        if User.objects.filter(username=request.POST.get('first_name')).exists():
            messages.error(request, 'student already exists')
        else:
            user = User()
            user.username = f"{request.POST.get('first_name')}{Grade.objects.get(name=request.POST.get('grade')).code}".lower()
            user.password = make_password(request.POST.get('last_name'))
            user.save()
            student = Student()
            student.name = user
            grade = Grade.objects.get(name=request.POST.get('grade'))
            student.grade = grade
            student.save()
            student_profile = StudentProfile()
            student_profile.student = student
            student_profile.first_name = request.POST.get('first_name')
            student_profile.last_name = request.POST.get('last_name')
            student_profile.save()
            messages.success(request, 'Student Created successfully')
            return redirect('student_portal')
    context = {
        'grades' : grades
    }
    return render(request, 'student_portal.html', context)


# from app_name.models import RelatedModel

def teacher_portal(request):
    if not request.user.is_superuser:
        return redirect('portal')
    courses = Course.objects.all()
    if request.method == 'POST':
        if User.objects.filter(username=request.POST.get('username')).exists():
            messages.error(request, 'Teacher already exists')
        else:
            courseList = request.POST.getlist('courses')
            user = User()
            user.username = request.POST.get('username')
            user.password = make_password(request.POST.get('password'))
            user.save()
            teacher = Teacher()
            teacher.name = user
            teacher.save()
            teacher.course.set(courseList)
            teacher.save()
            messages.info(request, 'Teacher Created successfully')
            return redirect('teacher_portal')
    context = {
        'courses' : courses
    }
    return render(request, 'teacher_portal.html', context)

