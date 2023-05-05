from django.shortcuts import render,redirect
from Course.models import Course
from Scheme.models import Scheme,Image

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
        image = Image()
        image.name = request.POST.get('image_name')
        image.image = request.FILES.get('image')
        image.holder = scheme
        image.save()
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