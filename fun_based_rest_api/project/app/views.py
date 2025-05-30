
from .models import * 
from .serializers import * 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status

@api_view(['GET', 'POST'])  
def student_list(request): 
    if request.method=='GET':
        students = Student.objects.all() 
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data) 
    
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else: return Response(serializer.errors)

@api_view(['GET', 'PUT','DELETE','PATCH']) 
def student_detail(request,pk):
    id = Student.objects.filter(id=pk)
    if id:
        if request.method=='GET': 
            student=Student.objects.get(id=pk) 
            serializer = StudentSerializer(student) 
            return Response(serializer.data) 
        
        elif request.method=='PUT': 
            student=Student.objects.get(id=pk) 
            serializer = StudentSerializer(student,data=request.data) 
            if serializer.is_valid(): 
                serializer.save() 
                return Response(serializer.data) 
            else: return Response(serializer.errors) 
        
        elif request.method=='PATCH': 
            student=Student.objects.get(id=pk) 
            serializer = StudentSerializer(student,data=request.data,partial=True) 
            if serializer.is_valid(): 
                serializer.save() 
                return Response(serializer.data) 
            else: return Response(serializer.errors)
        
        elif request.method=='DELETE': 
                student=Student.objects.get(id=pk) 
                student.delete() 
                return Response({'msg':"Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    else:
        res = {'msg': 'id not present in Database'}
        return Response(res)