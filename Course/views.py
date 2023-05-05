from django.shortcuts import render
from Log.models import User,Teacher

def courses(request):
    user = User.objects.get(username=request.user)
    teacher = Teacher.objects.get(name=user.id)
    courses = teacher.course.all()
    context = {
        'courses' : courses
    }
    return render(request, 'courses.html', context)