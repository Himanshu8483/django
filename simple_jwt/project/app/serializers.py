from .models import *
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = "__all__"
        fields = ['id', 'name', 'age', 'city', 'active']
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"
class HODSerializer(serializers.ModelSerializer):
    class Meta:
        model = HOD
        fields = "__all__"
        
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"