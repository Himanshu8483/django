from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return redirect('/index/')
#     # return redirect('/index/? key = {value} & key2={value2}')

def index(request):
    print(request.method)
    print(request.GET)
    x= request.GET.get('name')
    y=request.GET.get('city')
    print(x,y)  
    
    return HttpResponse("<h1>Hello through Redirect</h1>")

def home(request):
    name, city = 'Himanshu', 'Rewa'
    # return redirect(f'/index/?name={name}&city={city}')
# other way of return 
    return redirect('/index/?name={}&city={}'.format(name, city))