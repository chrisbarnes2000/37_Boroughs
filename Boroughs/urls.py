from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from Boroughs.views import *

urlpatterns = [
    # Boroughs Pages list of all pages
    path('', Boroughs_Landing, name='boroughs_landing'),
    path('models/', Display_Boroughs_View.as_view(), name='boroughs'),

    # Create new Borough need to be logged in at min
    path('new/', Create_Borough_View.as_view(), name='create-borough'),

    # Contribution Pages to Upload images
    path('contribute/photo', Create_Photo_View.as_view(), name='image-upload'),

    # Success Page for redirects
    path('success/', success, name='success'),

    # ex: /Boroughs/chinatown/
    path('<str:slug>/', Detail_Borough_View.as_view(), name='borough-details'),

    # ex: /Boroughs/chinatown/edit/
    path('<str:slug>/edit/', Edit_Borough_View.as_view(), name='edit-borough'),

    # ex: /Boroughs/chinatown/delete/
    path('<str:slug>/delete/', Delete_Borough_View.as_view(), name='delete-borough'),

    # Vote Page for a boroughs photo
    # path('<str:slug>/vote/', vote, name='vote'),
]
