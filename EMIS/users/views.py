# views.py: Manages the output segment/response for the respective API request.


# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from .services import AuthService

# # For register/
# class RegisterView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         username = request.data.get('username', '')  # Default to empty string if not provided
#         email = request.data.get('email', '')  # Default to empty string
#         password = request.data.get('password', '')

#         extra_fields = {key: request.data[key] for key in ['phone_number'] if key in request.data}
        
#         # Pass empty email if not provided
#         user, message = AuthService.register_user(username, email, password, **extra_fields)

#         if not user:
#             return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

#         return Response({"message": message}, status=status.HTTP_201_CREATED)


# # For login/
# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         tokens, message = AuthService.login_user(username, password)
        
#         if not tokens:
#             return Response({"message": message}, status=status.HTTP_401_UNAUTHORIZED)

#         return Response({"tokens": tokens, "message": message}, status=status.HTTP_200_OK)

# # For logout/
# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         refresh_token = request.data.get("refresh_token")
#         message = AuthService.logout_user(refresh_token)
#         return Response({"message": message}, status=status.HTTP_200_OK)

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.generics import CreateAPIView, GenericAPIView
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from .serializers import RegistrationSerializer, LoginSerializer, LogoutSerializer
# from .services import AuthService

# class RegisterView(CreateAPIView):
#     serializer_class = RegistrationSerializer
#     permission_classes = [AllowAny]


# class LoginView(GenericAPIView):
#     serializer_class = LoginSerializer
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         username = serializer.validated_data['username']
#         password = serializer.validated_data['password']

#         tokens, message = AuthService.login_user(username, password)
        
#         if not tokens:
#             return Response({"message": message}, status=status.HTTP_401_UNAUTHORIZED)

#         return Response({"tokens": tokens, "message": message}, status=status.HTTP_200_OK)
    
# class LogoutView(GenericAPIView):
#     serializer_class = LogoutSerializer
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         refresh_token = serializer.validated_data["refresh_token"]
#         message = AuthService.logout_user(refresh_token)
        
#         return Response({"message": message}, status=status.HTTP_200_OK)

# from django.shortcuts import redirect, render
# from django.contrib.auth import logout as auth_logout
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.generics import CreateAPIView, GenericAPIView
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from .serializers import RegistrationSerializer, LoginSerializer, LogoutSerializer
# from .services import AuthService
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from rest_framework.views import APIView

# class RegisterView(CreateAPIView):
#     serializer_class = RegistrationSerializer
#     permission_classes = [AllowAny]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user, message = AuthService.register_user(**serializer.validated_data)
#         if not user:
#             return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

#         # Redirect to the dashboard after successful registration
#         return redirect('dashboard')

# class LoginView(GenericAPIView):
#     serializer_class = LoginSerializer
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         username = serializer.validated_data['username']
#         password = serializer.validated_data['password']

#         tokens, message = AuthService.login_user(username, password)
        
#         if not tokens:
#             return Response({"message": message}, status=status.HTTP_401_UNAUTHORIZED)

#         # Redirect to the dashboard after successful login
#         return redirect('dashboard')

# class LogoutView(GenericAPIView):
#     serializer_class = LogoutSerializer
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         refresh_token = serializer.validated_data["refresh_token"]
#         message = AuthService.logout_user(refresh_token)
        
#         return Response({"message": message}, status=status.HTTP_200_OK)

# Dashboard View
# def dashboard(request):
#     if not request.user.is_authenticated:
#         return redirect('login')  # Redirect unauthenticated users to the login page
#     return render(request, 'dashboard/dashboard.html', {'user': request.user})
# class DashboardView(APIView):
#     @method_decorator(login_required)  # Ensure only authenticated users can access the dashboard
#     def get(self, request):
#         return render(request, 'dashboard/dashboard.html', {'user': request.user})

from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .serializers import RegistrationSerializer, LoginSerializer
from .services import AuthService
from rest_framework.permissions import AllowAny, IsAuthenticated

class RegisterView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user, message = AuthService.register_user(**serializer.validated_data)
        if not user:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

        # Log the user in after registration
        login(request, user)
        return redirect('dashboard')

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)
        if not user:
            return Response({"message": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        # Log the user in
        login(request, user)

        # Redirect to the "next" URL or the dashboard
        next_url = request.GET.get('next', 'dashboard')
        return redirect(next_url)

class LogoutView(APIView):
    def post(self, request):
        logout(request)  # Clear the user's session
        # Redirect to the "next" URL or the dashboard
        next_url = request.GET.get('next', 'login')
        return redirect(next_url)
        # return redirect('login')  # Redirect to the login page

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context