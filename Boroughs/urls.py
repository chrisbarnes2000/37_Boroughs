from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from Boroughs.views import *

urlpatterns = [
    # Boroughs Pages list of all pages
    path('', display_boroughs.as_view(), name='boroughs'),

    # Contribution Page to Upload Images
    path('contribute/', image_upload_view, name='image_upload'),

    # Success Page for redirects
    path('success/', success, name='success'),

    # ex: delete/chinatown/
    path('delete/<str:slug>/', DeleteBorough.as_view(), name='delete-borough'),

    # ex: Boroughs/chinatown/
    path('<str:slug>/', BoroughDetailView.as_view(), name='borough-detail-page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
