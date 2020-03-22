from django.urls import path
from Our_API.views import BoroughList, BoroughDetail

urlpatterns = [
    path("list/", BoroughList.as_view(), name="Page_list"),
    path("<int:pk>/", BoroughDetail.as_view(), name="Page_detail"),
    # path("<str:slug>/", PageDetail.as_view(), name="Page_detail"),
]
