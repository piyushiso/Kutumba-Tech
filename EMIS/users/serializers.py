# serializers.py: How datas are sent and received? (Django data to JSON)

# from rest_framework import serializers
# from .models import CustomUser  # Import our custom user model

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'phone_number']

from rest_framework import serializers
from .models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,  # This prevents the password from being exposed in responses
        style={'input_type': 'password'}  # This makes it appear as a password field
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone_number']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number')
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True,  # This prevents the password from being exposed in responses
        style={'input_type': 'password'}  # This makes it appear as a password field
    )
    
class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()