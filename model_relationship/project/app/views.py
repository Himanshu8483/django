from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def aadhar(request):
    data = Aadhar.objects.all()
    # print (data)      
    # print (data.values())     # return in list form and only ther are values not keys
    print (data.values_list())
    
    data = Aadhar.objects.get(aadhar_no = 1234)
    print(data.created_by)
    print(data.alloted_date)
    x = data.xyz    # for reverse accessing
    print(x.name)
    print(x.email)
    print(x.contact)
    print(x.aadhar_no)
    
def citizen(request):
    data = Citizen.objects.all()
    print(data)
    print(data.values())
    print (data.values_list())  
    # data = Citizen.objects.get(name = 'him')
    data = Citizen.objects.get(id=1)
    print(data.name)
    print(data.email)
    print(data.contact)
    
    print(data.aadhar_no)
    
    x = data.aadhar_no  # for forward accessing
    print(x.aadhar_no)
    print(x.created_by)
    print(x.alloted_date)
