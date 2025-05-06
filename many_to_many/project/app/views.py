from django.shortcuts import render
from .models import *
# Create your views here.

def fuel(request):
    all_data = FuelModel.objects.all()

def car(request):
    car = CarModel.objects.get(car_name='SUV')