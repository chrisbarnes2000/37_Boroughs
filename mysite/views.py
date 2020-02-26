from django.contrib.sites import requests
from django.core.serializers import json
from django.shortcuts import render
from django.conf import settings
import os

def Index(request):
    # CENSUS_API = settings.CENSUS_BASEAPI % os.getenv('CENSUS_KEY')

    # # #call the API and collect the response
    # response = requests.get(CENSUS_API)

    # # #load the response into a JSON, ignoring the first element which is just field labels
    # formattedResponse = json.loads(response.text)[1:]
    formattedResponse = "Hello world"

    return render(request, 'index.html', {'Census': formattedResponse})

def About(request):
    return render(request, 'about.html')

def Creator(request):
    return render(request, 'creators.html')
