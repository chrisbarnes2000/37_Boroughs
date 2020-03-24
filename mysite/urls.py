#mysite URL Configuration
from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path, re_path

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from mysite.views import *

from rest_framework import routers
from Our_API.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    # Index/Landing Page
    path('', Index, name='index'),

    # Accounts app
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    # path('accounts/', include('allauth.urls')),

    # Admin Site
    path('Admin/', admin.site.urls),

    # API
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('boroughs-api/', include('Our_API.urls')),

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
