import requests
import json
import os

from django.conf import settings
from django.shortcuts import render

from census import Census
from us import states


def Index(request):
    c = Census(os.getenv('CENSUS_KEY'))
    Name = c.sf1.get(
        'NAME', geo={'for': 'place:67000', 'in': 'state:{}'.format(states.CA.fips)})
    Population = c.sf1.get(
        'P001001', geo={'for': 'place:67000', 'in': 'state:{}'.format(states.CA.fips)})
    Housing = c.sf1.get(
        'H001001', geo={'for': 'place:67000', 'in': 'state:{}'.format(states.CA.fips)})
    return render(request, 'index.html', {
        'Census_Name': Name[0]['NAME'] + " 2010",
        'Census_Pop': '{:,}'.format(int(Population[0]['P001001'])), 
        'Census_House': "{:,}".format(int(Housing[0]['H001001'])),
    })


def YelpBusinessSearch(request):
    api_key = os.getenv('Yelp_KEY')
    headers = {'Authorization': 'Bearer %s' % api_key}

    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term': 'bookstore', 'location': 'New York City'}

    req = requests.get(url, params=params, headers=headers)

    parsed = json.loads(req.text)
    # print(parsed)

    businesses = parsed["businesses"]

    for business in businesses:
        print("Name:", business["name"])
        print("Rating:", business["rating"])
        print("Address:", " ".join(business["location"]["display_address"]))
        print("Phone:", business["phone"])
        print("\n")

        id = business["id"]

        url = "https://api.yelp.com/v3/businesses/" + id + "/reviews"

        req = requests.get(url, headers=headers)

        parsed = json.loads(req.text)

        reviews = parsed["reviews"]

        print("--- Reviews ---")

        for review in reviews:
            print("User:", review["user"]["name"], "Rating:",
                review["rating"], "Review:", review["text"], "\n")


def About(request):
    return render(request, 'about.html')

def Creator(request):
    return render(request, 'creators.html')
