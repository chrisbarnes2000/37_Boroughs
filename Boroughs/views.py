from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from Boroughs.models import Borough, Photo
from django.views.generic import *
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

import requests
import json
import os

def logout_view(request):
    logout(request)


def Boroughs_Landing(request):
    return render(request, 'boroughs_landing.html')


class Create_Borough_View(CreateView):
    model = Borough
    fields = ['title', 'zipcode', 'content', 'main_img', 'sources']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class Create_Photo_View(CreateView):
    model = Photo
    fields = ['first_name', 'last_name', 'email', 'content', 'image', 'borough']
    # success_url = reverse_lazy('index')

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)


# def vote(request, borough_slug):
#     borough = get_object_or_404(Borough, slug=borough_slug)
#     try:
#         selected_photo = borough.photo_set.get(pk=request.POST['photo'])
#     except (KeyError, Photo.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'Boroughs/borough.html', {
#             'borough': Borough,
#             'error_message': "You didn't select a photo.",
#         })
#     else:
#         selected_photo.votes += 1
#         selected_photo.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('borough-details', slug=borough.slug))


class Display_Boroughs_View(ListView):
    template_name = 'Boroughs/display_boroughs.html'
    context_object_name = 'Boroughs'

    def get_queryset(self):
        return Borough.objects.all()


class Detail_Borough_View(DetailView):
    model = Borough
    template_name = 'Boroughs/borough.html'


def YelpBusinessSearch(request):
    api_key = os.getenv('Yelp_KEY')
    headers = {'Authorization': 'Bearer %s' % api_key}

    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term': 'bookstore', 'location': 'San Francisco'}

    req = requests.get(url, params=params, headers=headers)

    parsed = json.loads(req.text)

    businesses = parsed["businesses"]
    # print(businesses[0])

    # for business in businesses:
    #     print("Name:", business["name"])
    #     print("Rating:", business["rating"])
    #     print("Address:", " ".join(business["location"]["display_address"]))
    #     print("Phone:", business["phone"])
    #     print("\n")

    #     id = business["id"]

    #     url = "https://api.yelp.com/v3/businesses/" + id + "/reviews"

    #     req = requests.get(url, headers=headers)

    #     parsed = json.loads(req.text)

    #     reviews = parsed["reviews"]

    #     print("--- Reviews ---")

    #     for review in reviews:
    #         print("User:", review["user"]["name"], "Rating:",
    #             review["rating"], "Review:", review["text"], "\n")

    return render(request, 'Boroughs/display_businesses.html', {"Businesses": businesses})


class Edit_Borough_View(UpdateView):
    model = Borough
    fields = ['title', 'zipcode', 'content', 'main_img', 'sources']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class Delete_Borough_View(DeleteView):
    model = Borough
    success_url = reverse_lazy('index')


def success(request):
    return HttpResponse('successfully uploaded')


# def image_upload(request):
#     if request.method == 'POST':
#         image_file = request.FILES['image_file']
#         image_type = request.POST['image_type']
#         if settings.USE_S3:
#             if image_type == 'private':
#                 upload = UploadPrivate(file=image_file)
#             else:
#                 upload = Upload(file=image_file)
#             upload.save()
#             image_url = upload.file.url
#         else:
#             fs = FileSystemStorage()
#             filename = fs.save(image_file.name, image_file)
#             image_url = fs.url(filename)
#         return render(request, 'upload.html', {
#             'image_url': image_url
#         })
#     return render(request, 'upload.html')
