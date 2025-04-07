from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
    # return render(request, 'home.html')
    # data= {'name':'Himanshu', 'age': 22, 'quali': 'MTech'}
    # return render(request, 'home.html', data)
    
    # in list format 
    data= [{'name':'Himanshu', 'age': 22, 'quali': 'BTech'},
           {'name':'Vijay', 'age': 23, 'quali': 'BTech'},
           {'name':'Jatin', 'age': 24, 'quali': 'MA'},]
    return render(request, 'home.html', {'key1':data})
    

def cart(request):
    data= [{'name': 'Himanshu', 'age':22}]
    user= {'city':'Rewa', 'name': 'Vijay'}
    return render(request, 'home.html', {'key2':data, 'key3':user})
    

def index(request):
    return redirect('https://www.google.com')

def textcontent(request):
    return HttpResponse('<h1><s>Hello</s></h1>')

def js(request):
    return JsonResponse({'name': True, 'age': None, 'city': 'Rewa'})

# 02 apr
# def home1(request):
#     data= {'name':'him', 'age': 22, 'quali': 'MTech'}
#     x=3
#     return render(request, home1.html, data)