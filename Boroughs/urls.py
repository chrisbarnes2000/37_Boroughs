from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Boroughs.views import Index, About

urlpatterns = [
    path('', Index, name='index'),
    path('About/', About, name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
