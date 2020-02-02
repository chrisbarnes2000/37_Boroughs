from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render


def Index(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')


def image_upload_view(request):
    template_name = 'partials/image_upload_form.html'
    if request.method == 'POST':
        form = BoroughForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BoroughForm()
        return render(request, template_name, {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def display_boroughs(request):
    template_name = 'display_boroughs.html'
    if request.method == 'GET':
        Boroughs = Borough.objects.all()
        return render(request, template_name, {'Boroughs': Boroughs})