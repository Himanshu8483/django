from django.shortcuts import render
from app.models import Student, Admin, Professor, Worker
from app.serializers import StudentSerializer, AdminSerializer, ProfessorSerializer, WorkerSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny

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
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    
class WorkerViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    
    
    
    
    
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username
        })