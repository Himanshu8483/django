from .models import *
from rest_framework import serializers


# class StudentSerializer(serializers.Serializer): 
#     id = serializers.IntegerField(read_only=True) 
#     name = serializers.CharField(max_length=50)
#     age = serializers.CharField() 
#     city = serializer.CharField(max_length=50)
#     active = serializers.BooleanField(default=True)
    
#     def create(self,validated_data): 
#         return Student.objects.create(**validated_data) 
    
#     def update(self, instence, validated_data): 
#         instence.name = validated_data.get('name',instence.name) 
#         instence.age = validated_data.get('age',instence.age) 
#         instence.city = validated_data.get('city',instence.city) 
#         instence.active = validated_data.get('active',instence.active) 
#         instence.save() 
#         return instence

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = "__all__"
        fields = ['id', 'name', 'age', 'city', 'active']
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"
        
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"