from rest_framework import serializers
from .models import *
class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy
        # fields = "__all__"
        fields = ['id', 'name', 'address', 'number', 'payment']