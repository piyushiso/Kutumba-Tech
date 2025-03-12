# services.py: Handles all the business logic of the project. Separates the business logic from the rest of the code base.

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .repositories import UserRepository

class AuthService:
    @staticmethod
    def register_user(username, email, password, **extra_fields):
        if UserRepository.get_user_by_email(email):
            return None, "User with this email already exists."
        
        user = UserRepository.create_user(username=username, email=email, password=password, **extra_fields)
        return user, "User registered successfully."

    @staticmethod
    def login_user(username, password):
        user = authenticate(username=username, password=password)
        if not user:
            return None, "Invalid credentials."
        
        refresh = RefreshToken.for_user(user)
        return {
            # 'refresh': str(refresh),
            # 'access': str(refresh.access_token)
        }, "Login successful."

    @staticmethod
    def logout_user(refresh_token):
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the token (requires `rest_framework_simplejwt.token_blacklist` installed)
            return "Logout successful."
        except Exception:
            return "Invalid token."