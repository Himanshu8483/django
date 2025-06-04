# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from .models import *
# from .serializers import StudentSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# import io
# # def student_list(request):
# #     stu = Student.objects.all()
# #     serializer = StudentSerializer(stu, many=True)
    
# #     # return JsonResponse(serializer.data, safe=False) 
# # # or
# #     json_data = JSONRenderer().render(serializer.data)
# #     return HttpResponse(json_data, content_type='application/json')

# # def student_detail(request, pk):
# #     user = Student.objects.get(pk=pk)
# #     serializer = StudentSerializer(user)
# #     # json_data = JSONRenderer().render(serializer.data)
# #     # return HttpResponse(json_data, content_type='application/json')
# #     # or 
# #     return JsonResponse(serializer.data, safe=False)



# @csrf_exempt
# def student_list(request):
#     if request.method == 'POST':
#         json_data = request.body
#         print(json_data)
#         steam=io.BytesIO(json_data)
#         python_data = JSONParser().parse(steam)
#         serializer = StudentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Data Created'}
#             json_data= JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         else:
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data, content_type = 'application/json')

# def student_detail(request, pk):
#     user = Student.objects.get(pk=pk)
#     serializer = StudentSerializer(user)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data, content_type='application/json')
#     # or 
#     return JsonResponse(serializer.data, safe=False)




# from django.shortcuts import render
# from django.http import HttpResponse,JsonResponse
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# import io

# # Create your views here.

# @csrf_exempt
# def student_api(request):
#     """
#     Handles GET, POST, PUT, and DELETE requests for Student model.
#     """

#     if request.method == 'GET':
#         json_data = request.body
#         if json_data:
#             stream = io.BytesIO(json_data)
#             python_data = JSONParser().parse(stream)
#             id = python_data.get('id')
#             try:
#                 stu = Student.objects.get(id=id)
#                 serializer = StudentSerializer(stu)
#                 return JsonResponse(serializer.data, safe=False)
#             except Student.DoesNotExist:
#                 return JsonResponse({'msg': 'Student not found'}, status=404)
#         else:
#             stu_all = Student.objects.all()
#             serializer = StudentSerializer(stu_all, many=True)
#             return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'msg': 'Data Created'}, status=201)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         try:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu, data=python_data, partial=True)  # partial=True for partial updates
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse({'msg': 'Data Updated'}, status=200)
#             return JsonResponse(serializer.errors, status=400)
#         except Student.DoesNotExist:
#             return JsonResponse({'msg': 'Student not found'}, status=404)

#     elif request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         if id:
#             try:
#                 stu = Student.objects.get(id=id)
#                 stu.delete()
#                 return JsonResponse({'msg': 'Data Deleted'}, status=200)
#             except Student.DoesNotExist:
#                 return JsonResponse({'msg': 'Student not found'}, status=404)
#         else:
#             return JsonResponse({'msg': 'ID not provided'}, status=400)
#     return JsonResponse({'msg': 'Invalid HTTP method'}, status=405)



# @csrf_exempt
# def student_list(request):
#     if request.method == 'POST':
#         json_data = request.body
#         print(json_data)
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer =StudentSerializer(data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
    
# @csrf_exempt
# def student_detail(request,pk):
#     # print(pk)
#     # print(request.method)
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         new_python_data = JSONParser().parse(stream)
#         old_data = Student.objects.get(id=pk)
#         # serializer = StudentSerializer(old_data, data=python_data, partial = True)
#         serializer = StudentSerializer(old_data, data=new_python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Updated !!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

#     elif request.method == 'PATCH':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         stu = Student.objects.get(id=pk)
#         serializer = StudentSerializer(stu, data=python_data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Partially Updated...!!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')  
 
#     elif request.method == 'DELETE':
#         stu = Student.objects.filter(id=pk)
#         if stu:
#             stu = Student.objects.get(id=pk)
#             stu.delete()
#             res = {'msg': 'Data Deleted!!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         else:
#             res = {'msg': 'Not Present in database!!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')





from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io 






# serialize and deesrialize



@csrf_exempt
def student_list(request): 
    if request.method=='GET':
        stu = Student.objects.all()
        print(type(stu))
        # print("stu=",stu)
        # print("stu.values()=",stu.values())
        # print("stu.values_list()=",stu.values_list())
        # print("stu.values_list(col1,col2,col3)=",stu.values_list('name','city','rollno'))
        serializer = StudentSerializer(stu, many=True)
        # print("Serializer=",serializer)
        # print(serializer.data)
        json_data = JSONRenderer().render(serializer.data)
        # print("Json_data=",json_data)
        return HttpResponse(json_data, content_type='application/json')
        # when we send json data from views then content type must be "application/json"
        # return JsonResponse(serializer.data,safe=False)
        # first argument of JsonResponse should be a dict,otherwise set safe=False

    elif request.method=='POST':
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        print(stream)
        python_data=JSONParser().parse(stream)
        print(python_data)
        serializer=StudentSerializer(data=python_data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            res={'msg':"Data Created"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        else:
            json_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application/json')

    elif request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        new_python_data=JSONParser().parse(stream)
        old_id=new_python_data.get('id')
        old_data=Student.objects.get(id=old_id)
        serializer=StudentSerializer(old_data,data=new_python_data)

        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    elif request.method=='PATCH':
        json_data=request.body
        stream=io.BytesIO(json_data)
        new_python_data=JSONParser().parse(stream)
        id=new_python_data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=new_python_data,partial=True)

        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Partially Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    elif request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        if id:
            stu=Student.objects.get(id=id)
            stu.delete()
            res={'msg':'Data Deleted'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        res={'msg':'Id not present in Database'}
        return JsonResponse(res)






def student_detail(request, pk):
    user = Student.objects.get(pk=pk)
    # print(type(user))
    # print("Stu_Name=",user.name)
    # print("Stu_City=",user.city)
    # print("Stu_Rollno=",user.rollno)
    serializer = StudentSerializer(user)
    # print("Serializer=",serializer)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    # when we send json data from views then content type must be "application/json"
    return JsonResponse(serializer.data,safe=False)
    # first argument of JsonResponse should be a dict,otherwise set safe=False
