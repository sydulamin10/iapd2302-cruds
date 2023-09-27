from django.shortcuts import render, redirect
from .models import *
import os
from django.contrib import messages

def index(request):

    if request.method == 'GET':
        search = request.GET.get('src')
        if search:
            PROFILE = profile.objects.filter(name__icontains = search)
        elif search == "None":
            return redirect('home')
        else:
            PROFILE = profile.objects.all()

    return render(request, 'index.html', locals())  # used locals() for POST method


def delete(request, id):
    prof = profile.objects.get(id=id)
    if prof.image != 'def.png':
        os.remove(prof.image.path)
    prof.delete()
    messages.warning(request, "Account Deleted.")

    return redirect('index')


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.FILES.get('img')
        gender = request.POST.get('gender')
        number = request.POST.get('num')
        birth = request.POST.get('birth')
        if profile.objects.filter(name=name).exists():
            messages.warning(request, "Another account already exixt with this name.")
            return redirect('create')
        elif profile.objects.filter(email=email).exists():
            messages.warning(request, "Another account already exixt with this email.")
            return redirect('create')
        else:
            if image:
                prof = profile.objects.create(name=name, email=email, image=image, phone=number, deate_of_birth=birth)
                prof.save()
                messages.success(request, "Account created.")
                return redirect('index')
            else:
                prof = profile.objects.create(name=name, email=email, phone=number, deate_of_birth=birth)
                prof.save()
                messages.success(request, "Account created.")
                return redirect('index')

    return render(request, 'create.html')

def single_prof(request, id):
    prof = profile.objects.get(id=id)
    return render (request , 'profile_details.html', locals())

def update_prof(request, id):
    prof = profile.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.FILES.get('img')
        gender = request.POST.get('gender')
        number = request.POST.get('num')
        birth = request.POST.get('birth')
        if name:
            if image != 'def.png':
                os.remove(prof.image.path)
                prof.image = image
            prof.name = name
            prof.email = email
            prof.gender = gender
            prof.phone = number
            prof.deate_of_birth = birth
            prof.save()
            messages.success(request, "Profile Updated!")
            return redirect('index')
        else:
            messages.success(request, "Got an error")

    return render (request,'update.html', locals())


def new (request):
    pass

def new2(request):
    pass

