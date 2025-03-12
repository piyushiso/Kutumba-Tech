# models.py: Where data is stored in your project?

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):  # Extending Django's built-in User model
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username