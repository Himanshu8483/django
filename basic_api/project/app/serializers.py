from rest_framework import serializers
from .models import Student
# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=50)
#     city = serializers.CharField(max_length=50)
#     contact = serializers.IntegerField()
    
    
    
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.city = validated_data.get('city', instance.city)
#         instance.contact = validated_data.get('contact', instance.contact)
#         instance.save()
#         return instance
    
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = "__all__"
        fields = ['id', 'name', 'city', 'contact']