# repositories.py: Handles all the database related actions, and separates database logic/segment from rest of the code base.

from .models import CustomUser

class UserRepository:
    @staticmethod
    def create_user(**kwargs):
        return CustomUser.objects.create_user(**kwargs)

    @staticmethod
    def get_user_by_email(email):
        return CustomUser.objects.filter(email=email).first()