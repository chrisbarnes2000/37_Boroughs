from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Boroughs.views import index

urlpatterns = [
    path('', index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
