from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.http import HttpResponse
from Boroughs.models import Borough
from django.views.generic import *
from Boroughs.forms import *

def logout_view(request):
    logout(request)


class Display_Boroughs_View(ListView):
    template_name = 'Boroughs/display_boroughs.html'
    context_object_name = 'Boroughs'

    def get_queryset(self):
        return Borough.objects.all()


class Detail_Borough_View(DetailView):
    model = Borough
    template_name = 'Boroughs/borough.html'


class Edit_Borough_View(UpdateView):
    model = Borough
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class Delete_Borough_View(DeleteView):
    model = Borough
    success_url = reverse_lazy('index')


def image_upload_view(request):
    template_name = 'partials/image_upload_form.html'
    if request.method == 'POST':
        form = BoroughForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BoroughForm()
        return render(request, template_name, {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
