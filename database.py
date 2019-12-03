from employee import Employee
from jobtitle import Jobtitle
from level import Level
from service import Service

class Database:
    def __init__(self):
        self.employees = {}
        self.jobtitles = {}
        self._last_employee_key = 0
        self._last_jobtitle_key = 0
###EMPLOYEES
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
        return 
####JOBTITLES
    def add_jobtitle(self, jobtitle):
        self._last_jobtitle_key += 1
        self.jobtitles[self._last_jobtitle_key] = jobtitle
        return self._last_jobtitle_key

    def delete_jobtitle(self, jobtitle_key):
        if jobtitle_key in self.jobtitles:
            del self.jobtitles[jobtitle_key]
    
    def get_jobtitle(self, jobtitle_key):
        jobtitle = self.jobtitles.get(jobtitle_key)
        if jobtitle is None:
            return None
        jobtitle_ = Jobtitle(jobtitle.title)
        return jobtitle_
    
    def get_jobtitles(self):
        jobtitles = []
        for jobtitle_key, jobtitle in self.jobtitles.items():
            jobtitle_ = Jobtitle(jobtitle.title)
            jobtitles.append((jobtitle_key, jobtitle_))
        return 
########LEVELS
    def add_level(self, level):
        self._last_level_key += 1
        self.levels[self._last_level_key] = level
        return self._last_level_key

    def delete_level(self, level_key):
        if level_key in self.levels:
            del self.levels[level_key]
    
    def get_level(self, level_key):
        level = self.levels.get(level_key)
        if level is None:
            return None
        level_ = Level(level.title)
        return level_
    
    def get_levels(self):
        levels = []
        for level_key, level in self.levels.items():
            level_ = Level(level.title)
            levels.append((level_key, level_))
        return 
######SERVICE

