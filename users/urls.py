# users/urls.py
from django.urls import path
from users.views import SignUp, Profile

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/<str:username>/', Profile.as_view(), name='profile'),
]
