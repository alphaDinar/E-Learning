from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Course.models import Course
from Scheme.models import Scheme,Image,Video,Passage


@login_required
def schemes(request,slug):
    course = Course.objects.get(slug = slug)
    context = {
        'course' : course,
        'schemes' : course.get_schemes()
    }
    return render(request, 'schemes.html', context)

def use_scheme(request, slug):
    scheme = Scheme.objects.get(slug=slug)
    course = scheme.course
    context ={
        'scheme' : scheme,
        'course' : course
    }
    return render(request, 'use_scheme.html', context)

def edit_scheme(request, slug):
    scheme = Scheme.objects.get(slug=slug)
    course = scheme.course
    if request.method == 'POST':
        print(request.POST.get('res_type'))
        if request.POST.get('res_type') == 'image':
            image = Image()
            image.name = request.POST.get('res_name')
            image.image = request.FILES.get('res')
            image.holder = scheme
            image.save()
        elif request.POST.get('res_type') == 'video':
            video = Video()
            video.name = request.POST.get('res_name')
            video.video = request.FILES.get('res')
            print(video.video)
            video.holder = scheme
            video.save()
        elif request.POST.get('res_type') == 'passage':
            print(request.POST)
            passage = Passage()
            passage.title = request.POST.get('passage_title')
            passage.body = request.POST.get('passage_body')
            if request.FILES.get('res_thumb'):
                passage.thumb = request.FILES.get('res_thumb') 
            passage.holder = scheme
            passage.save()
        else:
            print('noen')
    context ={
        'scheme' : scheme,
        'course' : course
    }   
    return render(request, 'edit_scheme.html', context)

def delete_image(request, slug,id):
    scheme = Scheme.objects.get(slug=slug)
    image = scheme.get_images().get(id=id)
    image.delete()
    return redirect('edit_scheme_page',slug)

def delete_video(request, slug,id):
    scheme = Scheme.objects.get(slug=slug)
    video = scheme.get_videos().get(id=id)
    video.delete()
    return redirect('edit_scheme_page',slug)