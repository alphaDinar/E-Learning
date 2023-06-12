from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User,Student,Teacher
from Course.models import Course,Grade

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

