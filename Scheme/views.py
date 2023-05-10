from django.middleware.csrf import get_token
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from Course.models import Course
from Scheme.models import Scheme,Image,Video,Passage,Slide
import json


@login_required
def schemes(request,slug):
    course = Course.objects.get(slug = slug)
    schemes = course.get_schemes()
    pend_count = schemes.filter(status = 'pending').count()
    act_count = schemes.filter(status = 'active').count()
    comp_count = schemes.filter(status = 'completed').count()
    status = {'pend_count' : pend_count, 'act_count' : act_count, 'comp_count' : comp_count}
    context = {
        'course' : course,
        'schemes' : schemes,
        'status' : status
    }
    return render(request, 'schemes.html', context)

def use_scheme(request, slug):
    scheme = Scheme.objects.get(slug=slug)
    token = get_token(request)
    context ={
        'scheme' : scheme,
        'token' : token
    }
    return render(request, 'use_scheme.html', context)

def save_scheme_slide(request):
    if request.method == 'POST':
        data = request.body
        json_data = json.loads(data)
        
        if json_data['data'][1]:
            slide_title = json_data['data'][1]
        else:
            slide_title = 'New Slide'
        if Slide.objects.filter(title=slide_title).exists():
            slide = Slide.objects.get(title=slide_title)
            print(json_data['data'][2])
            slide.con = json_data['data'][2]   
            print(slide.con)
            slide.save() 
        else:
            Slide.objects.create(title=slide_title, con=json_data['data'][2], holder=Scheme.objects.get(id=json_data['data'][0])).save()
    return JsonResponse({'test':'good'})

def edit_scheme(request, slug):
    scheme = Scheme.objects.get(slug=slug)
    token = get_token(request)
    if request.method == 'POST':
        if request.POST.get('res_type') == 'image':
            res_name = request.POST.get('res_name')
            if Image.objects.filter(name=res_name).exists():
                messages.info(request, f'Image named {res_name} already exists')
            else:
                image = Image()
                image.name = res_name
                image.image = request.FILES.get('res')
                image.holder = scheme
                image.save()
                messages.info(request, 'images added successfully')
        elif request.POST.get('res_type') == 'video':
            res_name = request.POST.get('res_name')
            if Video.objects.filter(name=res_name).exists():
                messages.info(request, f'Video named {res_name} already exists')
            else:
                video = Video()
                video.name = request.POST.get('res_name')
                video.video = request.FILES.get('res')
                video.holder = scheme
                video.save()
                messages.info(request, 'video added successfully')
        elif request.POST.get('res_type') == 'passage':
            if(request.POST.get('passage_id')):
                passage = Passage.objects.get(id=request.POST.get('passage_id'))
                passage.title = request.POST.get('passage_title')
                passage.body = request.POST.get('passage_body')
                if request.FILES.get('passage_thumb'):
                    passage.thumb = request.FILES.get('passage_thumb')
                passage.save()
                messages.info(request, 'changes have been made')
            else:
                res_name = request.POST.get('passage_title')
                if Passage.objects.filter(title=res_name).exists():
                    messages.info(request, f'Passage named {res_name} already exists')
                else:
                    passage = Passage()
                    passage.title = res_name
                    passage.body = request.POST.get('passage_body')
                    if request.FILES.get('passage_thumb'):
                        passage.thumb = request.FILES.get('passage_thumb') 
                    passage.holder = scheme
                    passage.save()
                    messages.info(request, 'passage added successfully')
        else:
            print('noen')
    context ={
        'scheme' : scheme,
        'token' : token
    }   
    return render(request, 'edit_scheme.html', context)


def delete_scheme_image(request):
    if request.method == 'POST':
        data = request.body
        json_data = json.loads(data)
        res_id = json_data['data']
        Image.objects.get(id=res_id).delete()
    return JsonResponse({'test':'good'})

def delete_scheme_video(request):
    if request.method == 'POST':
        data = request.body
        json_data = json.loads(data)
        res_id = json_data['data']
        Video.objects.get(id=res_id).delete()
    return JsonResponse({'test':'good'})

def delete_scheme_passage(request):
    if request.method == 'POST':
        data = request.body
        json_data = json.loads(data)
        res_id = json_data['data']
        Passage.objects.get(id=res_id).delete()
    return JsonResponse({'test':'good'})

# @csrf_exempt
def hello(request):
    if request.method == 'POST':
        print(request.POST)
    return JsonResponse({'test':'good'})

def test(request):
    token = get_token(request)
    context = {
        'token' : token
    }
    return render(request,'test.html', context)

def head(request):
    return render(request, 'head.html')