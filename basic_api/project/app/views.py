from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .serializers import *
# Create your views here.
def stu_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
def stduent_detail(request, pk):
    user = Student.objects.get(pk=pk)
    serializer = StudentSerializer(user)
    return JsonResponse(serializer.data, safe=False)