from django.shortcuts import render
from django.middleware.csrf import get_token
from django.http import JsonResponse
from Log.models import Student
from Course.models import Course
from Scheme.models import Scheme
from Quiz.models import Quiz,Score
import json


def student_dash(request):
    return render(request, 'student_dash.html')

def student_quizes(request):
    student = Student.objects.get(name=request.user)
    courses = student.grade.get_courses().all()
    context = {
        'courses' : courses
    }
    return render(request, 'student_quizes.html', context)

def student_get_quizes_schemes(request,slug):
    course = Course.objects.get(slug=slug)
    schemes = Scheme.objects.filter(course=course)
    context = {
        'course' : course,
        'schemes' : schemes
    }
    return render(request, 'student_get_quizes_schemes.html', context)

def student_get_quizes(request,slug):
    scheme = Scheme.objects.get(slug=slug)
    context = {
        'scheme' : scheme
    }
    return render(request, 'student_get_quizes.html', context)

def student_start_quiz(request,slug):
    quiz = Quiz.objects.get(slug=slug)
    token = get_token(request)  
    context = {
        'quiz' : quiz,
        'token' : token
    }
    return render(request, 'student_start_quiz.html', context)

def mark_quiz(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        quiz = Quiz.objects.get(id=json_data['data'][0])
        choice_box = json_data['data'][1]
        total_score = len(choice_box)
        score_count = 0
        for i in range(total_score):
            cor_ans = json.loads(quiz.marking_scheme)[i]['cor_ans']
            choice = choice_box[i]
            if choice == cor_ans:
                score_count = score_count + 1
        percent = (score_count * 100)/total_score
        score = Score()
        score.quiz_title = quiz.title
        score.quiz_con = quiz.con
        score.quiz_ans_box = quiz.marking_scheme
        score.mark = "{:.2f}".format(percent) 
        score.choice_box = json.dumps(choice_box)
        score.save()
    return JsonResponse({'info': 'redirect', 'link' : f'/student_quiz_results/{score.id}' })

def student_quiz_results(request,id):
    score = Score.objects.get(id=id)
    context = {
        'score' : score
    }
    return render(request, 'student_quiz_results.html', context)