from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import profile, User
from .serializers import MyModelSerializer, USerSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = profile.objects.all()
    serializer_class = MyModelSerializer


class UsersView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = USerSerializer