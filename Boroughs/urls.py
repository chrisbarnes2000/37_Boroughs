from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.urls import path

from Boroughs.views import *

admin.autodiscover()

# login_required()

urlpatterns = [
    # Boroughs Pages list of all pages
    path('', Boroughs_Landing, name='boroughs_landing'),
    path('models/', Display_Boroughs_View.as_view(), name='boroughs'),

    # Create new Borough need to be logged in at min
    path('new/', staff_member_required(Create_Borough_View.as_view()), name='create-borough'),

    # Contribution Pages to Upload images
    path('contribute/photo', Create_Photo_View.as_view(), name='image-upload'),

    # Success Page for redirects
    path('success/', success, name='success'),

    # Yelp Api
    # path('businesses/', YelpBusinessSearch, name='yelp-business-search'),

    # ex: /Boroughs/chinatown/
    path('<str:slug>/', Detail_Borough_View.as_view(), name='borough-details'),

    # ex: /Boroughs/chinatown/edit/
    path('<str:slug>/edit/', login_required(Edit_Borough_View.as_view()), name='edit-borough'),

    # ex: /Boroughs/chinatown/delete/
    path('<str:slug>/delete/', staff_member_required(Delete_Borough_View.as_view()), name='delete-borough'),

    # Vote Page for a boroughs photo
    path('<str:slug>/vote/', Detail_Borough_View.vote, name='vote'),
]
