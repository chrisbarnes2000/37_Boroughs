# users/views.py
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, TemplateView
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, Subscribe, ContactForm
# from django.conf import settings
# settings.AUTH_USER_MODEL
from .models import CustomUser as User

from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def emailView(request):
    template_name = "users/email.html"

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,
                          ['sf.37.boroughs@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, template_name, {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')


# def subscribe(request):
#     sub = Subscribe()
#     if request.method == 'POST':
#         sub = Subscribe(request.POST)
#         subject = 'Welcome to 37 Boroughs'
#         message = 'Hope you are enjoying your our website'
#         recepient = str(sub['Email'].value())
#         send_mail(subject,
#                   message, EMAIL_HOST_USER, [recepient], fail_silently=False)
#         return render(request, 'registration/success.html', {'recepient': recepient})
#     return render(request, 'index.html', {'form': sub})


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
