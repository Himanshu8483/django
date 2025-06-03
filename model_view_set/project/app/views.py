from django.shortcuts import render
from app.models import Student
from app.serializers import StudentSerializer
from rest_framework import viewsets
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer