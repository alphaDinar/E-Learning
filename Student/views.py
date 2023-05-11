from django.shortcuts import render

def student_dash(request):
    return render(request, 'student_dash.html')