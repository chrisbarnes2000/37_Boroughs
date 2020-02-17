from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.http import HttpResponse
from Boroughs.models import Borough, Photo
from django.views.generic import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Upload, UploadPrivate

def logout_view(request):
    logout(request)


class Create_Borough_View(CreateView):
    model = Borough
    fields = ['title', 'content', 'main_img']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class Create_Photo_View(CreateView):
    model = Photo
    fields = ['first_name', 'last_name', 'email', 'content', 'image', 'borough']

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)


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
    fields = ['title', 'content', 'main_img']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class Delete_Borough_View(DeleteView):
    model = Borough
    success_url = reverse_lazy('index')


def success(request):
    return HttpResponse('successfully uploaded')


def image_upload(request):
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        image_type = request.POST['image_type']
        if settings.USE_S3:
            if image_type == 'private':
                upload = UploadPrivate(file=image_file)
            else:
                upload = Upload(file=image_file)
            upload.save()
            image_url = upload.file.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
        return render(request, 'upload.html', {
            'image_url': image_url
        })
    return render(request, 'upload.html')
