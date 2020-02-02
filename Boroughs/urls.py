from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from Boroughs.views import *

urlpatterns = [
    path('', Index, name='index'),
    path('About/', About, name='about'),
    path('Boroughs/', display_boroughs, name='Boroughs'),
    path('image_upload/', image_upload_view, name='image_upload'),
    path('success/', success, name='success'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
