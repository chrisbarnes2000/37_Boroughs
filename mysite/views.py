from django.shortcuts import render
import os
import dotenv
dotenv.load_dotenv('.env')

USE_S3 = os.getenv('USE_S3')
DEBUG = os.getenv('DEBUG')

def Index(request):
    return render(request, 'index.html', {
        'Mode': USE_S3, 'Debug': DEBUG
    })

def About(request):
    return render(request, 'about.html')

def Creator(request):
    return render(request, 'creators.html')
