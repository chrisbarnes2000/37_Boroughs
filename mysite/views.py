from django.shortcuts import render
import os
import dotenv
dotenv.load_dotenv('.env')

USE_S3 = os.getenv('USE_S3')

def Index(request):
    return render(request, 'index.html', {
        'Mode': USE_S3
    })

def About(request):
    return render(request, 'about.html')

def Creator(request):
    return render(request, 'creators.html')
