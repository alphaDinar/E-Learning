from django.shortcuts import render,redirect
from django.middleware.csrf import get_token
from django.contrib import messages
from django.http import JsonResponse,HttpResponseRedirect
from Log.models import Student
from Course.models import Course
from Scheme.models import Scheme
from Quiz.models import Quiz
from .models import StudentProfile,Score
import json


def checkStudent(request):
    if Student.objects.filter(name=request.user).exists():
        return True
    else:
        return False
    

def student_dash(request):
    if not checkStudent(request):
        messages.error(request,'Login with Student Account')
        return redirect('homepage')
    else:
        student = Student.objects.get(name=request.user)
        student_profile = StudentProfile.objects.get(student=student)
    context = {
        'student' : student,
        'student_profile' : student_profile
    }
    return render(request, 'student_dash.html', context)

def student_quizes(request):
    if not checkStudent(request):
        messages.error(request,'Login with Student Account')
        return redirect('homepage')
    else:
        student = Student.objects.get(name=request.user)
        courses = student.grade.get_courses().all()
    context = {
        'courses' : courses
    }
    return render(request, 'student_quizes.html', context)

def student_get_quizes_schemes(request,slug):
    if not checkStudent(request):
        messages.error(request,'Login with Student Account')
        return redirect('homepage')
    else:
        course = Course.objects.get(slug=slug)
        schemes = Scheme.objects.filter(course=course)
    context = {
        'course' : course,
        'schemes' : schemes
    }
    return render(request, 'student_get_quizes_schemes.html', context)

def student_get_quizes(request,slug):
    if not checkStudent(request):
        messages.error(request,'Login with Student Account')
        return redirect('homepage')
    else:
        scheme = Scheme.objects.get(slug=slug)
    context = {
        'scheme' : scheme
    }
    return render(request, 'student_get_quizes.html', context)

def student_start_quiz(request,slug):
    if not checkStudent(request):
        messages.error(request,'Login with Student Account')
        return redirect('homepage')
    else:
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
        student = Student.objects.get(name=request.user)
        if Score.objects.filter(student=student).filter(quiz=quiz).exists():
            pass
        else:
            score = Score()
            score.student = student
            score.quiz = quiz
            score.quiz_con = quiz.con
            score.quiz_ans_box = quiz.marking_scheme
            score.mark = "{:.2f}".format(percent) 
            score.choice_box = json.dumps(choice_box)
            score.save()
    return JsonResponse({'info': 'redirect', 'link' : f'/student_quiz_results/{score.slug}' })

def student_quiz_results(request,slug):
    score = Score.objects.get(slug=slug)
    context = {
        'score' : score
    }
    return render(request, 'student_quiz_results.html', context)

def student_assessment(request):
    return render(request, 'student_assessment.html')