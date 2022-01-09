import os

from census import Census
from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import render
from sentry_sdk import capture_message
from us import states


def Index(request):
    c = Census(os.getenv("CENSUS_KEY"))
    Name = c.sf1.get(
        "NAME", geo={"for": "place:67000", "in": "state:{}".format(states.CA.fips)}
    )
    Population = c.sf1.get(
        "P001001", geo={"for": "place:67000", "in": "state:{}".format(states.CA.fips)}
    )
    Housing = c.sf1.get(
        "H001001", geo={"for": "place:67000", "in": "state:{}".format(states.CA.fips)}
    )
    return render(
        request,
        "index.html",
        {
            "Census_Name": Name[0]["NAME"] + " 2010",
            "Census_Pop": "{:,}".format(int(Population[0]["P001001"])),
            "Census_House": "{:,}".format(int(Housing[0]["H001001"])),
        },
    )


def Creator(request):
    return render(request, "creators.html")


# def my_custom_bad_request_view(request, *args, **kwargs):
#     capture_message("Bad Request Page!", level="error")
#     return render(request, "400.html")


# def my_custom_permission_denied_view(request, *args, **kwargs):
#     capture_message("Permission Denied Page!", level="error")
#     return render(request, "403.html")


# def my_custom_page_not_found_view(request, *args, **kwargs):
#     capture_message("Page not found!", level="error")
#     return render(request, "404.html")


# def my_custom_error_view(request, *args, **kwargs):
#     capture_message("Internal Server Error Page!", level="error")
#     return render(request, "500.html")
