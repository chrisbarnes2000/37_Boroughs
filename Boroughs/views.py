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

def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('success')
    else:
        form = HotelForm()
        return render(request, 'hotel_image_form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
