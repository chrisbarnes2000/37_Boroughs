#mysite URL Configuration
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from mysite.views import *

urlpatterns = [
    # Index/Landing Page
    path('', Index, name='index'),

    # Admin Site
    path('Admin/', admin.site.urls),

    # API
    # path('api/', include('Our_API.urls')),

    # Boroughs urls
    path('Boroughs/', include('Boroughs.urls')),

    # Creators Page
    path('Creators/', Creator, name='creators'),

    path('media/<str:path>', serve,
        {'document_root': settings.MEDIA_ROOT}),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG and settings.USE_S3 == False:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
