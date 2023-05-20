from django.shortcuts import render
from django.middleware.csrf import get_token
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from Course.models import Course,Grade
from Log.models import Student,User,Teacher
import json

def supermanager(request):
    return render(request, 'supermanager.html')

def super_student_assessment(request):
    grades = Grade.objects.all()
    context = {
        'grades' : grades
    }
    return render(request, 'super_student_assessment.html', context)


def super_get_student_assessment(request,slug):
    grade = Grade.objects.get(slug=slug)
    context = {
        'grade' : grade
    }
    return render(request, 'super_get_student_assessment.html', context)

def super_add_student(request):
    grades = Grade.objects.all()
    context = {
        'grades' : grades
    }
    return render(request, 'super_add_student.html', context)

def super_get_students(request,slug):
    grade = Grade.objects.get(slug=slug)
    token = get_token(request)
    if request.method == 'POST':
        if request.POST.get('type') == 'new':
            if User.objects.filter(username=request.POST.get('first_name')).exists():
                messages.error(request, 'student already exists')
            else:
                user = User()
                user.username = f"{request.POST.get('first_name')}{User.objects.count() + 1}".lower()
                user.password = make_password(request.POST.get('last_name'))
                user.save()
                student = Student()
                student.name = user
                grade = grade
                student.grade = grade
                student.first_name = request.POST.get('first_name')
                student.last_name = request.POST.get('last_name')
                student.save()
                messages.success(request, f'{user.username} Created successfully')
        else :
            user = User.objects.get(username=request.POST.get('name'))
            user.password = make_password(request.POST.get('last_name'))
            user.save()
            student = Student.objects.get(name=user)
            student.first_name = request.POST.get('first_name')
            student.last_name = request.POST.get('last_name')
            student.save()
            messages.success(request, f'{student} Updated successfully')
    context = {
        'grade' : grade,
        'token' : token
    }
    return render(request, 'super_get_students.html', context)

def super_delete_student(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        User.objects.get(username=json_data['data']).delete()
    return JsonResponse({'info':'success'})

def super_add_teacher(request):
    teachers = Teacher.objects.all()
    courses = Course.objects.all()
    if request.method == 'POST':
        if request.POST.get('type') == 'new':
            if User.objects.filter(username=request.POST.get('username')).exists():
                messages.error(request, 'Username already Taken')
            else:
                if(request.POST.getlist('courses')):
                    courseList = request.POST.getlist('courses')
                    user = User()
                    user.username = request.POST.get('username')
                    user.password = make_password(request.POST.get('password'))
                    user.save()
                    teacher = Teacher()
                    teacher.name = user
                    teacher.password = request.POST.get('password')
                    teacher.save()
                    teacher.course.set(courseList)
                    teacher.save()
                    messages.info(request, f'{user.username} Created successfully')
                else:
                    messages.error(request, 'Select at least one Course')
        else:
            courseList = request.POST.getlist('courses')
            user = User.objects.get(username=request.POST.get('name'))
            user.username = request.POST.get('username')
            user.password = make_password(request.POST.get('password'))
            user.save()
            teacher = Teacher.objects.get(name=user)
            teacher.password = request.POST.get('password')
            teacher.course.set(courseList)
            teacher.save()
            messages.success(request, f'{user} Updated successfully')
    context = {
        'teachers' : teachers,
        'courses' : courses
    }
    return render(request, 'super_add_teacher.html', context)

# def super_delete_student(request):
#     if request.method == 'POST':
#         json_data = json.loads(request.body)
#         User.objects.get(username=json_data['data']).delete()
#     return JsonResponse({'info':'success'})


def super_grades(request):
    grades = Grade.objects.all()
    token = get_token(request)
    if request.method == 'POST':
        if Grade.objects.filter(name=request.POST.get('grade')).exists() or Grade.objects.filter(code=request.POST.get('code')).exists():
            messages.error(request, 'Grade already exists')
        else:
            if request.POST.get('type') == 'new':
                grade = Grade()
                grade.name = request.POST.get('grade')
                grade.code = request.POST.get('code')
                grade.save()
            else:
                grade = Grade.objects.get(name=request.POST.get('grade'))
                grade.name = request.POST.get('grade')
                grade.code = request.POST.get('code')
                grade.save()
    context = {
        'grades' : grades,
        'token' : token
    }
    return render(request, 'super_grades.html', context)

def super_delete_grade(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        Grade.objects.get(id=json_data['data']).delete()
    return JsonResponse({'test':'good'})

def super_get_grade(request,slug):
    grade = Grade.objects.get(slug=slug)
    token = get_token(request)
    if request.method == 'POST':
        if Course.objects.filter(grade=grade).filter(subject=request.POST.get('subject')).exists():
            messages.error(request, 'Course already exists')
        else:
            if request.POST.get('type') == 'new':
                course = Course()
                course.subject = request.POST.get('subject')
                course.grade = grade
                course.save()
                messages.success(request, 'Course added successfully')
            else:
                course = Course.objects.get(id=request.POST.get('id'))
                course.subject = request.POST.get('subject')
                course.save()
                messages.success(request, 'Course updated successfully')
    context = {
        'grade' : grade,
        'token' : token
    }
    return render(request, 'super_get_grade.html', context)

def super_delete_course(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        Course.objects.get(id=json_data['data']).delete()
    return JsonResponse({'test':'good'})

def super_test(request):
    student = Student.objects.get(name=request.user)
    context = {
        'student' : student
    }
    return render(request, 'super_test.html', context)

