from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    
    # return JsonResponse(serializer.data, safe=False) 
# or
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

def student_detail(request, pk):
    user = Student.objects.get(pk=pk)
    serializer = StudentSerializer(user)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    # or 
    return JsonResponse(serializer.data, safe=False)