# users/urls.py
from django.urls import path
from users.views import SignUp, Profile

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('<str:path>/profile/', Profile.as_view(), name='profile'),
]
