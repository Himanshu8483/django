from django.shortcuts import render
from  .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def first(request):
    data = Student.objects.all()[0:5]
    print(data)
    return render(request, 'index.html', {'data':data})

def last(request):
    data = Student.objects.order_by('-s_no')[:5]
    print(data)
    print(data)
    return render(request, 'index.html', {'data': data})
    
def all(request):
    data = Student.objects.all()
    print(data)
    print(data)
    return render(request, 'index.html', {'data': data})
    
def asc(request):
    data = Student.objects.order_by('name')        
    print(data)
    print(data)
    return render(request, 'index.html', {'data': data})
    
def desc(request):
    data = Student.objects.order_by('-name')        
    print(data)
    print(data)
    return render(request, 'index.html', {'data': data})    
