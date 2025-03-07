from .models import Employee

# Repository Pattern: Segment to engage with database logic. Separates database logic with other segments.

class EmployeeRepository:
    # Static methods to avoid object instantiation.
    @staticmethod
    # Method to return all the entries from the database.
    def get_all():
        return Employee.objects.all()
    
    # Method to return the entry with the given ID from the database.
    @staticmethod
    def get_by_id(emp_id):
        return Employee.objects.filter(id=emp_id).first()
    
    # Method to create a new entry from the database.
    @staticmethod
    def create(data):
        return Employee.objects.create(**data)
    
    # Method to update an entry from the database.
    @staticmethod
    def update(emp_id, data):
        Employee.objects.filter(id=emp_id).update(**data)
    
    # Method to delete an entry from the database.
    @staticmethod
    def delete(emp_id):
        Employee.objects.filter(id=emp_id).delete()