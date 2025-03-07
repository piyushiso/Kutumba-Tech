from django.db import models

# Models: Clarifying the database data & datatype of employees.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    department = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Meta Data: Stating database table name.
    class Meta:
        db_table = 'employee_data'

    def __str__(self):
        return self.name