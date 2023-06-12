from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.contrib import messages
from celery import shared_task
from Course.models import Course
from Scheme.models import Scheme
from Quiz.models import Quiz,Assignment
from Student.models import QuizScore 
import json,datetime

def capitalize(string):
    return string[0].upper() + string[1:]

def quizes(request,slug):
    course = Course.objects.get(slug=slug)
    if request.user.is_manager:
        return redirect('schemes_page', course.slug)
    schemes = course.get_schemes()
    quiz_count = 0
    for scheme in schemes:
        quiz_count = quiz_count + scheme.get_quizes().count()
    print(quiz_count)
    context ={
        'course' : course,
        'schemes' : schemes,
        'quiz_count' : quiz_count,
    }
    return render(request, 'quizes.html', context)

def assignments(request,slug):
    course = Course.objects.get(slug=slug)
    if request.user.is_manager:
        return redirect('schemes_page', course.slug)
    context ={
        'course' : course,
        'schemes' : course.get_schemes(),
        # 'quiz_count' : quiz_count,
    }
    return render(request, 'assignments.html', context)

def get_quizes(request,slug):
    scheme = Scheme.objects.get(slug=slug)
    course = scheme.course
    if request.method == 'POST':
        title = capitalize(request.POST.get('title'))
        if not Quiz.objects.filter(topic=scheme).filter(title=title).exists():
            Quiz.objects.create(topic=scheme,title=title, course=scheme.course).save()
        else:
            messages.error(request, f'Quiz with title {title} already exists')
    context ={
        'course' : course,
        'scheme' : scheme,
    }
    return render(request, 'get_quizes.html', context)

def get_assignments(request,slug):
    scheme = Scheme.objects.get(slug=slug)
    course = scheme.course
    if request.method == 'POST':
        title = capitalize(request.POST.get('title'))
        if not Assignment.objects.filter(topic=scheme).filter(title=title).exists():
            Assignment.objects.create(topic=scheme,title=title, course=scheme.course).save()
        else:
            messages.error(request, f'Quiz with title {title} already exists')
    context ={
        'course' : course,
        'scheme' : scheme,
    }
    return render(request, 'get_assignments.html', context)

def use_quiz(request,slug):
    quiz = Quiz.objects.get(slug=slug)
    token = get_token(request)  
    if request.method == 'POST':
        quiz.title = request.POST.get('title')
        quiz.duration = request.POST.get('duration')
        quiz.save()
    context = {
        'token' : token,
        'quiz' : quiz,
    }
    return render(request, 'use_quiz.html', context)

def use_assignment(request,slug):
    assignment = Assignment.objects.get(slug=slug)
    token = get_token(request)  
    if request.method == 'POST':
        assignment.title = request.POST.get('title')
        date = request.POST.get('date')
        time = request.POST.get('time')
        deadline = datetime.datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
        assignment.deadline = deadline
        assignment.save()
    context = {
        'token' : token,
        'assignment' : assignment,
    }
    return render(request, 'use_assignment.html', context)

def toggle_assignment(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        assignment = Assignment.objects.get(id=json_data['data'][0])
        if assignment.protection == 'locked':
            assignment.protection = 'unlocked'
        else:
            assignment.status = 'locked'
        assignment.save()
    return JsonResponse({'test':'good'})

def delete_quiz(request,slug):
    quiz = Quiz.objects.get(slug=slug)
    scheme = quiz.topic.slug
    quiz.delete()
    return redirect('get_quizes_page', scheme)

def delete_assignment(request,slug):
    assignment = Assignment.objects.get(slug=slug)
    scheme = assignment.topic.slug
    assignment.delete()
    return redirect('get_assignments_page', scheme)

def set_quiz(request,slug):
    token = get_token(request)
    quiz = Quiz.objects.get(slug=slug)
    context = {
        'quiz' : quiz,
        'token' : token
    }
    return render(request, 'set_quiz.html', context)

def set_assignment(request,slug):
    token = get_token(request)
    assignment = Assignment.objects.get(slug=slug)
    context = {
        'assignment' : assignment,
        'token' : token
    }
    return render(request, 'set_assignment.html', context)

def save_quiz(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        quiz = Quiz.objects.get(id=json_data['data'][0])
        quiz.con = json_data['data'][1]
        quiz.marking_scheme = json_data['data'][2]
        quiz.save()
    return JsonResponse({'info':'reload'})

def save_assignment(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        assignment = Assignment.objects.get(id=json_data['data'][0])
        assignment.con = json_data['data'][1]
        assignment.marking_scheme = json_data['data'][2]
        assignment.save()
    return JsonResponse({'info':'reload'})

def delete_session(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        quiz = Quiz.objects.get(id=json_data['data'][0])
        quiz.status = 'locked'
        quiz.save()
    return JsonResponse({'test':'deleted'})


def assess_quiz(request, slug):
    quiz = Quiz.objects.get(slug=slug)
    course = quiz.topic.course
    quiz_scores = []
    for student in course.grade.get_students():
        if QuizScore.objects.filter(student=student).filter(quiz=quiz).order_by('-mark').exists():
            quiz_scores.append(QuizScore.objects.filter(student=student).filter(quiz=quiz).order_by('-mark').first())
        else:
            quiz_scores.append(student)
    print(quiz_scores)
    context = {
        'course' : course,
        'quiz' : quiz,
        'quiz_scores' : quiz_scores,
    }
    return render(request, 'assess_quiz.html', context)