from .repositories import EmployeeRepository

# Service Pattern: Segment to engage with business logic. Separates business logic with other segments.

class EmployeeService:
    @staticmethod
    # Method to retrieve all the employee data.
    def list_employees():
        return EmployeeRepository.get_all()
    
    # Method to retrieve an employee data with the given ID.
    @staticmethod
    def get_employee(emp_id):
        return EmployeeRepository.get_by_id(emp_id)
    
    # Method to create an employee.
    @staticmethod
    def create_employee(data):
        return EmployeeRepository.create(data)
    
    # Method to update an employee with the given ID.
    @staticmethod
    def update_employee(emp_id, data):
        return EmployeeRepository.update(emp_id, data)
    
    # Method to delete an employee with the given ID.
    @staticmethod
    def delete_employee(emp_id):
        return EmployeeRepository.delete(emp_id)