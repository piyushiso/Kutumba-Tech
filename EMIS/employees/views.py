from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeeSerializer
from .services import EmployeeService
# from .models import Employee

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    # permission_classes = [IsAuthenticated]

    # GET: .../employees/
    def get_queryset(self):
        return EmployeeService.list_employees()
    
    # POST: .../employees/
    def perform_create(self, serializer):
        serializer.save()
    
    # PUT: .../employees/{id}
    def perform_update(self, serializer):
        serializer.save()
    
    # DELETE: .../employees/{id}
    def perform_destroy(self, instance):
        instance.delete()