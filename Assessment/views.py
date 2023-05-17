from django.shortcuts import render
from Course.models import Course

def assessment(request,slug):
    course = Course.objects.get(slug=slug)
    schemes = course.get_schemes()
    quiz_count = 0
    # for scheme in schemes:
        # quiz_count = quiz_count + scheme.get_quizes().count()
    print(quiz_count)
    context ={
        'course' : course,
        'schemes' : schemes,
        'quiz_count' : quiz_count,
    }
    return render(request, 'assessment.html', context)
