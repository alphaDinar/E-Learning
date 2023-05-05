from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('courses_page')
    return render(request, 'index.html')