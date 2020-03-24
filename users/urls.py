# users/urls.py
from django.urls import path
from users.views import SignUp, Profile
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/<str:username>/',  login_required(Profile.as_view()), name='profile'),
]
