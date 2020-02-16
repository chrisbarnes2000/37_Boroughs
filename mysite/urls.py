#mysite URL Configuration
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from mysite.views import *

urlpatterns = [
    # Index/Landing Page
    path('', Index, name='index'),

    # About Page
    path('About/', About, name='about'),

    # Admin Site
    path('Admin/', admin.site.urls),

    # Boroughs urls
    path('Boroughs/', include('Boroughs.urls')),

    # Creators Page
    path('Creatord/', Creator, name='creators'),
]