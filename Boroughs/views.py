import requests
import json
import os

from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail, mail_admins
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import *

from Boroughs.models import Borough, Photo


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
        mail_admins(
            "New Photo For",
            form.borough,
            fail_silently=False,
            connection=None,
            html_message=None
        )
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
    paginate_by = 9

    def get_queryset(self):
        return Borough.objects.all()


class Detail_Borough_View(DetailView):
    model = Borough
    template_name = 'Boroughs/borough.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        api_key = os.getenv('Yelp_KEY')
        headers = {'Authorization': 'Bearer %s' % api_key}

        url = 'https://api.yelp.com/v3/businesses/search'
        params = {'term': 'bookstore', 'location': 'San Francisco'}

        req = requests.get(url, params=params, headers=headers)

        parsed = json.loads(req.text)

        businesses = parsed["businesses"]

        # Add in a QuerySet of all the businesses
        context['Businesses'] = businesses
        return context

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

        # 'Boroughs/display_businesses.html',
        # return render(request, template_name, {"display": display, "Businesses": businesses})

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
