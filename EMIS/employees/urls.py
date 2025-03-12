from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter()
# Connects .../employees/... with the resepctive view from EmployeeViewSet class (employees/views.py)
router.register(r'', EmployeeViewSet, basename='employees')  

urlpatterns = [
    path('', include(router.urls)),  
]