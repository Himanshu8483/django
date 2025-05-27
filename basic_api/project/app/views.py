from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io
# def student_list(request):
#     stu = Student.objects.all()
#     serializer = StudentSerializer(stu, many=True)
    
#     # return JsonResponse(serializer.data, safe=False) 
# # or
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type='application/json')

# def student_detail(request, pk):
#     user = Student.objects.get(pk=pk)
#     serializer = StudentSerializer(user)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data, content_type='application/json')
#     # or 
#     return JsonResponse(serializer.data, safe=False)



@csrf_exempt
def student_list(request):
    if request.method == 'POST':
        json_data = request.body
        print(json_data)
        steam = io.BytesIO(json_data)
        python_data = JSONParser().parse(steam)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    # Default response for other methods (like GET)
    return HttpResponse(
        JSONRenderer().render({'msg': 'Only POST method allowed'}),
        content_type='application/json',
        status=405  # Method Not Allowed
    )

def student_detail(request, pk):
    user = Student.objects.get(pk=pk)
    serializer = StudentSerializer(user)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    # or 
    return JsonResponse(serializer.data, safe=False)