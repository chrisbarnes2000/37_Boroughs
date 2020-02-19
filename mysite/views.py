from django.shortcuts import render
import os
import dotenv
dotenv.load_dotenv('.env')

def Index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Creator(request):
    return render(request, 'creators.html')
