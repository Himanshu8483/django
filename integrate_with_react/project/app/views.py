from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.
class BuyViewSet(viewsets.ModelViewSet):
    queryset=Buy.objects.all()
    serializer_class=BuySerializer