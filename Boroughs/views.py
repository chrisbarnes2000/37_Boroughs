import requests
import json
import os
from django.conf import settings
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail, mail_admins
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import *

from Boroughs.models import Borough, Photo
from census import Census
from us import states


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
        # mail_admins(
        #     "New Photo For",
        #     [self.borough, self.image],
        #     fail_silently=False,
        #     connection=None,
        #     html_message=None
        # )
        # form.instance.author = self.request.user
        return super().form_valid(form)


# Msg.attach(‘file_name.type’, content, ‘MIME / type’) 


class Display_Boroughs_View(ListView):
    template_name = 'Boroughs/display_boroughs.html'
    context_object_name = 'Boroughs'
    paginate_by = 9

    def get_queryset(self):
        return Borough.objects.all()


class Detail_Borough_View(DetailView):
    model = Borough
    template_name = 'Boroughs/borough.html'

    def vote(self, request):
        borough = get_object_or_404(Borough, slug=self.slug)
        try:
            selected_photo = borough.photo_set.get(pk=request.POST['photo'])
        except (KeyError, Photo.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'Boroughs/borough.html', {
                'borough': Borough,
                'error_message': "You didn't select a photo.",
            })
        else:
            selected_photo.votes += 1
            selected_photo.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('borough-details', slug=borough.slug))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

# -------------------YELP API RENDERING-------------------------------------

        api_key = os.getenv('Yelp_KEY')

        headers = {'Authorization': 'Bearer %s' % api_key}
        url = 'https://api.yelp.com/v3/businesses/search'
        params = {'term': 'bookstore', 'location': 'San Francisco'}
        req = requests.get(url, params=params, headers=headers)

        parsed = json.loads(req.text)
        businesses = parsed["businesses"]
        # for business in businesses:
        #     id = business["id"]
        #     url = "https://api.yelp.com/v3/businesses/" + id + "/reviews"
        #     req = requests.get(url, headers=headers)
        #     parsed = json.loads(req.text)
        #     reviews = parsed["reviews"]
        #     print("--- Reviews ---")

# -----------------CENSUS API RENDERING---------------------------------------

        c = Census(os.getenv('CENSUS_KEY'))
        tracts = context['object'].tract
        Census_House = []
        Census_Pop = []
        Population = 0
        Housing = 0

        for tract in tracts.split():
            tract = tract.strip(',')
            # Name = c.sf1.state_county_tract('NAME', states.CA.fips, '075', tract)
            Population_json = c.sf1.state_county_tract('P001001', states.CA.fips, '075', tract)
            pop_val = int(Population_json[0]['P001001'])
            Census_Pop.append('{:,}'.format(pop_val))
            Population += pop_val

            Housing_json = c.sf1.state_county_tract('H001001', states.CA.fips, '075', tract)
            house_val = int(Housing_json[0]['H001001'])
            Census_House.append("{:,}".format(house_val))
            Housing += house_val

# -----------------Add to QuerySet---------------------------------------

        # Yelp context
        context['Businesses'] = businesses
        # context['reviews'] = reviews

        # Census context
        # context['Census_Name'] = Name[0]['NAME'] + " 2010"
        context['Census_Pop'] = Census_Pop
        context['Census_House'] = Census_House
        context['Total_Population'] = Population
        context['Total_Housing'] = Housing
        context['tracts'] = tracts
        return context


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
