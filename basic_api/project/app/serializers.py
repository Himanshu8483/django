from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)
    contact = serializers.IntegerField()
    