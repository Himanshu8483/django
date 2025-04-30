from django.shortcuts import render
from .models import *
# Create your views here.
def aadhar(request):
    data = Aadhar.objects.all()
    # print (data)
    # print (data.values())     # return in list form and only ther are values not keys
    print (data.values_list())
def citizen(request):
    data = Aadhar.objects.all()
    print (data)