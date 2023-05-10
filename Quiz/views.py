from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
from django.http import JsonResponse
from Course.models import Course
from Scheme.models import Scheme
from Quiz.models import Quiz,Score
import json

def quizes(request,slug):
    course = Course.objects.get(slug=slug)
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

def get_quizes(request,slug):
    scheme = Scheme.objects.get(slug=slug)
    course = scheme.course
    if request.method == 'POST':
        title = request.POST.get('title')
        topic = scheme
        duration = request.POST.get('duration')
        level = request.POST.get('level')
        Quiz.objects.create(title=title, topic=topic, duration=duration, level=level).save()
    context ={
        'course' : course,
        'scheme' : scheme,
    }
    return render(request, 'get_quizes.html', context)

def use_quiz(request,slug):
    quiz = Quiz.objects.get(slug=slug)
    token = get_token(request)  
    if request.method == 'POST':
        title = request.POST.get('title')
        duration = request.POST.get('duration')
        level = request.POST.get('level')
        quiz.title = title
        quiz.duration = duration
        quiz.level = level
        quiz.save()
    context = {
        'quiz' : quiz,
        'token' : token
    }
    return render(request, 'use_quiz.html', context)

def delete_quiz(request,slug):
    quiz = Quiz.objects.get(slug=slug)
    scheme = quiz.topic.slug
    quiz.delete()
    return redirect('get_quizes_page', scheme)

def set_quiz(request,slug):
    token = get_token(request)
    quiz = Quiz.objects.get(slug=slug)
    context = {
        'quiz' : quiz,
        'token' : token
    }
    return render(request, 'set_quiz.html', context)

def save_quiz(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        quiz = Quiz.objects.get(id=json_data['data'][0])
        quiz.con = json_data['data'][1]
        quiz.marking_scheme = json_data['data'][2]
        quiz.save()
    return JsonResponse({'info':'reload'})

def test_quiz(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        quiz = Quiz.objects.get(id=json_data['data'][0])
        choice_box = json_data['data'][1]
        total_score = len(choice_box)
        score = 0
        for cor_ans in json.loads(quiz.marking_scheme):
            for choice in choice_box:
                if cor_ans['cor_ans'] == choice:
                    score = score + 1
        percent = (score * 100)/total_score
    return JsonResponse({'info': percent})



def start_quiz(request,slug):
    quiz = Quiz.objects.get(slug=slug)
    token = get_token(request)  
    context = {
        'quiz' : quiz,
        'token' : token
    }
    return render(request, 'start_quiz.html', context)

def mark_quiz(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        quiz = Quiz.objects.get(id=json_data['data'][0])
        choice_box = json_data['data'][1]
        total_score = len(choice_box)
        score_count = 0
        for cor_ans in json.loads(quiz.marking_scheme):
            for choice in choice_box:
                if cor_ans['cor_ans'] == choice:
                    score_count = score_count + 1
        percent = (score_count * 100)/total_score
        score = Score()
        score.quiz_title = quiz.title
        score.quiz_con = quiz.con
        score.quiz_ans_box = quiz.marking_scheme
        score.mark = "{:.2f}".format(percent) 
        score.choice_box = json.dumps(choice_box)
        score.save()
    return JsonResponse({'info': 'redirect', 'link' : f'/quiz_results/{score.id}' })

def quiz_results(request,id):
    score = Score.objects.get(id=id)
    context = {
        'score' : score
    }
    return render(request, 'quiz_results.html', context)