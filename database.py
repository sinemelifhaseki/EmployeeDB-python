from employee import Employee

class Database:
    def __init__(self):
        self.employees = {}
        self._last_employee_key = 0

    def add_employee(self, employee):
        self._last_employee_key += 1
        self.employees[self._last_employee_key] = employee
        return self._last_employee_key

    def delete_employee(self, employee_key):
        if employee_key in self.employees:
            del self.employees[employee_key]

    def get_employee(self, employee_key):
        employee = self.employees.get(employee_key)
        if employee is None:
            return None
        employee_ = Employee(employee.title, age=employee.age)
        return employee_

    def get_employees(self):
        employees = []
        for employee_key, employee in self.employees.items():
            employee_ = Employee(employee.title, age=employee.age)
            employees.append((employee_key, employee_))
        return employees