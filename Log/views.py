from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import User

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    if user.is_superuser:
                        return redirect('supermanager_page')
                    elif user.is_student:
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




