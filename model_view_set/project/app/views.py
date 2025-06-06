from django.shortcuts import render
from app.models import Student, Admin, Professor, Worker
from app.serializers import StudentSerializer, AdminSerializer, ProfessorSerializer, WorkerSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly  

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class ProfessorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    
class AdminViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    
class WorkerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer