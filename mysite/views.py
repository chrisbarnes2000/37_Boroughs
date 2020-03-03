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
        'Census_Name': Name[0]['NAME'],
        'Census_Pop': '{:,}'.format(int(Population[0]['P001001'])), 
        'Census_House': "{:,}".format(int(Housing[0]['H001001'])),
    })



def About(request):
    return render(request, 'about.html')

def Creator(request):
    return render(request, 'creators.html')
