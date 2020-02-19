from django.shortcuts import render
import os
import dotenv
dotenv.load_dotenv('.env')

DEBUG = os.getenv('DEBUG')

def Index(request):
    return render(request, 'index.html', {'DEBUG':DEBUG})

def About(request):
    return render(request, 'about.html')

def Creator(request):
    return render(request, 'creators.html')
