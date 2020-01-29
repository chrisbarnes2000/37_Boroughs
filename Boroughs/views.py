from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render

def Index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')
