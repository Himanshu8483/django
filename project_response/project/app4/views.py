from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def app4(request):
    data= {'name': 'Himanshu', 'age':20, 'quali':"Btech"}
    data= {'name': True, 'age':False, 'quali':None}
    return JsonResponse(data)
    