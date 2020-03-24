# users/views.py
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, TemplateView
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
# from django.conf import settings
# settings.AUTH_USER_MODEL
from .models import CustomUser as User

class SignUp(CreateView):
    # form_class = UserCreationForm
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class Profile(TemplateView):
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = get_object_or_404(
            User, username=kwargs['username'])
        return context
