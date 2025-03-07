from rest_framework import serializers
from .models import Employee

# Converts complex model instances to further readable/useable data.

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'