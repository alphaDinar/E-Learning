from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import User

import requests

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

import json

def zoom(request):
    url = "https://api.zoom.us/v2/users/me/meetings"

    payload = ""
    headers = {
    'Authorization': 'Bearer eyJzdiI6IjAwMDAwMSIsImFsZyI6IkhTNTEyIiwidiI6IjIuMCIsImtpZCI6ImMyNTJmZTAzLWU4ZGQtNGIzZC05YWJiLWZkMTUzMjY4ZmQ1OSJ9.eyJ2ZXIiOjksImF1aWQiOiJjOGFkYjRmNzZkZmJlYzAwYmZjMTFmMmFjY2JlZDgyNiIsImNvZGUiOiI3eThQM3F2WjVsNzJ5Zndzd2RFVHVxX1MwTzVEYXpxckEiLCJpc3MiOiJ6bTpjaWQ6akxIVm1fZVlRbFNrSzFDMnZxdnJrdyIsImdubyI6MCwidHlwZSI6MCwidGlkIjowLCJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJYaVp6NmlndlRYLU1JbDBUWjZUelBBIiwibmJmIjoxNjg2ODQxNzk1LCJleHAiOjE2ODY4NDUzOTUsImlhdCI6MTY4Njg0MTc5NSwiYWlkIjoiTUlZd3VyTDdSYkNXN1dHdXFrZGFiQSJ9.jFZpZ67vos7En7oBGoHCQ9fVR8LU_NEFiK_ndMtRgyZsZrAWJJDdTzNXRaVDznRHHW83_mD2ktb7Lex_H8MBkg',
    'Cookie': 'TS018dd1ba=01d5510adcd1c2aa3888e654015204b9d90743c63270d63ed8510cb58ef6b76fd049d939db2720d79cfa0fec677cadedf849f6c283; __cf_bm=I4e.Lvx03W7tRk5YuC0sB2NuBpuvWCh3JGzkPvapZ8g-1686841480-0-Ac+tH6hJf3LqZyNWjBRGRVZHCbXmh4mDDmJLpGXT6vLfmnhsBDeaqX6Dd1PkRziS6boqrRr+UnPqXxE3ipaX8UU=; _zm_mtk_guid=00621b875dd84ccfa4d11e2b792ae920; _zm_page_auth=us05_c_LTPebZvvRdqV8BdIh2jvEQ; _zm_ssid=us05_c_ot8XWe4aT_6spkKL3FUmmA; TS01f92dc5=01d5510adcd1c2aa3888e654015204b9d90743c63270d63ed8510cb58ef6b76fd049d939db2720d79cfa0fec677cadedf849f6c283; cred=E6F136B1232732BBC6E027A6620D5AC7'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    context = {
        'meetings' : response.text
    }
    return render(request, 'zoom.html',context)




