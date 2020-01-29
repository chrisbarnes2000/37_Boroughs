from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.http import HttpResponse
# from django.shortcuts import render

def index(result):
    return HttpResponse("Hello, world. You're at the Boroughs index.")
