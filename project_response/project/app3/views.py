from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app3(request):
    return HttpResponse('<h1 style=color:blue><s>This is django class</s></h1>')
    # first="""Hello This is 
    # django Class"""
    # return HttpResponse(first)