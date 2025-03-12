# urls.py: Handles the routes.

from django.urls import path, include
from .views import RegisterView, LoginView, DashboardView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),  # Dashboard route
    # path('accounts/', include('django.contrib.auth.urls')),  # Add Django's auth URLs
]