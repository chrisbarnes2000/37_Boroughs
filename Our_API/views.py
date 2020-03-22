from rest_framework import generics, viewsets, permissions
from django.contrib.auth.models import User, Group

from Boroughs.models import Borough, Photo
from Our_API.serializer import UserSerializer, GroupSerializer, BoroughSerializer, PhotoSerializer


class BoroughList(generics.ListCreateAPIView):
    queryset = Borough.objects.all()
    serializer_class = BoroughSerializer
    # permission_classes = [permissions.IsAuthenticated]


class BoroughDetail(generics.RetrieveDestroyAPIView):
    queryset = Borough.objects.all()
    serializer_class = BoroughSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
