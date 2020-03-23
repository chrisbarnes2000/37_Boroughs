# users/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .forms import CustomUserCreationForm


class SignUp(CreateView):
    form_class = UserCreationForm
    # form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class Profile(DetailView):
    model = User
    template_name = 'registration/profile.html'
