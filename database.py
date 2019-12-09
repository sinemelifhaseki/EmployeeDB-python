import psycopg2 as dbapi2
from employee import Employee
from jobtitle import Jobtitle
from level import Level
from service import Service
from workchart import Workchart
from transportation import Transportation

class Database:
    def __init__(self, dbfile):
        self.dbfile = dbfile
    
###EMPLOYEES
    def add_employee(self, employee):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO PERSON (NAME, AGE, GENDER, HEIGHT, WEIGHT) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (employee.name, employee.age, employee.gender, employee.height, employee.weight))
            connection.commit()
            employee_key = cursor.lastrowid
        return employee_key

    def delete_employee(self, employee_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM PERSON WHERE (ID = %s)"
            cursor.execute(query, (employee_key,))
            connection.commit()

    def update_employee(self, employee_key, name, age, gender, height, weight):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE PERSON SET NAME = %s, AGE = %s, GENDER = %s, HEIGHT = %s, WEIGHT = %s WHERE (ID = %s)"
            cursor.execute(query, (name, age, gender, height, weight, employee_key))
            connection.commit()
        return employee_key

    def get_employee(self, employee_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT NAME, AGE, GENDER, HEIGHT, WEIGHT FROM PERSON WHERE (ID = %s)"
            cursor.execute(query, (employee_key,))
            name, age, gender, height, weight = cursor.fetchone()
        employee_ = Employee(name, age, gender, height, weight)
        return employee_

    def get_employees(self):
        employees = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, NAME, AGE, GENDER, HEIGHT, WEIGHT FROM PERSON ORDER BY ID"
            cursor.execute(query)
            for employee_key, name, age, gender, height, weight in cursor:
                employees.append((employee_key, Employee(name, age, gender, height, weight)))
        return employees
####JOBTITLES
    def add_jobtitle(self, jobtitle):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO JOBTITLES (JOBNAME, IS_EXECUTIVE, DEPARTMENT, IS_ACTIVE, TO_BE_HIRED) VALUES (%s, %s, %s,%s,%s)"
            cursor.execute(query, (jobtitle.title, jobtitle.is_executive,jobtitle.department, jobtitle.is_active, jobtitle.to_be_hired))
            connection.commit()
            jobtitle_key = cursor.lastrowid
        return jobtitle_key

    def delete_jobtitle(self, jobtitle_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM JOBTITLES WHERE (ID = %s)"
            cursor.execute(query, (jobtitle_key,))
            connection.commit()

    def update_jobtitle(self, jobtitle_key, title, is_executive, department, is_active, to_be_hired):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE JOBTITLES SET JOBNAME = %s, IS_EXECUTIVE = %s, DEPARTMENT = %s, IS_ACTIVE = %s, TO_BE_HIRED= %s WHERE (ID = %s)"
            cursor.execute(query, (name, age, gender, height, weight, employee_key))
            connection.commit()
        return jobtitle_key
    
    def get_jobtitle(self, jobtitle_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT JOBNAME, IS_EXECUTIVE, DEPARTMENT, IS_ACTIVE, TO_BE_HIRED FROM JOBTITLES WHERE (ID = %s)"
            cursor.execute(query, (jobtitle_key,))
            title,is_executive,department,is_active,to_be_hired = cursor.fetchone()
        jobtitle_ = Jobtitle(title,is_executive,department,is_active,to_be_hired)
        return jobtitle_
    
    def get_jobtitles(self):
        jobtitles = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, JOBNAME, IS_EXECUTIVE, DEPARTMENT, IS_ACTIVE, TO_BE_HIRED FROM JOBTITLES ORDER BY ID"
            cursor.execute(query)
            for jobtitle_key, title, is_executive, department, is_active, to_be_hired in cursor:
                jobtitles.append((jobtitle_key, Jobtitle(title,is_executive,department,is_active,to_be_hired)))
        return jobtitles
########LEVELS
    def add_level(self, level):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO LEVEL (LEVELNAME, EXPERIENCE_YEAR_NEEDED, BONUS_SALARY, IS_DIRECTOR, IS_MANAGER) VALUES (%s, %s, %s, %s, %s);"
            cursor.execute(query, (level.title, level.experience, level.bonus_salary, level.is_director, level.is_manager))
            connection.commit()
            level_key = cursor.lastrowid
        return level_key

    def delete_level(self, level_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM LEVEL WHERE (ID = %s)"
            cursor.execute(query, (level_key,))
            connection.commit()

    def update_level(self, level_key, title, experience, bonus_salary, is_director, is_manager):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE LEVEL SET LEVELNAME = %s, EXPERIENCE_YEAR_NEEDED = %s, BONUS_SALARY = %s, IS_DIRECTOR = %s, IS_MANAGER= %s WHERE (ID = %s)"
            cursor.execute(query, (level_key, title, experience, bonus_salary, is_director, is_manager))
            connection.commit()
        return level_key
    
    def get_level(self, level_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT LEVELNAME, EXPERIENCE_YEAR_NEEDED, BONUS_SALARY, IS_DIRECTOR, IS_MANAGER FROM LEVEL WHERE (ID = %s)"
            cursor.execute(query, (level_key,))
            title, experience, bonus_salary, is_director, is_manager = cursor.fetchone()
        level_ = Level(title, experience, bonus_salary, is_director, is_manager)
        return level_
    
    def get_levels(self):
        levels = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, LEVELNAME, EXPERIENCE_YEAR_NEEDED, BONUS_SALARY, IS_DIRECTOR, IS_MANAGER FROM LEVEL ORDER BY ID"
            cursor.execute(query)
            for level_key, title, experience, bonus_salary, is_director, is_manager in cursor:
                levels.append((level_key, Level(title, experience, bonus_salary, is_director, is_manager)))
        return levels
######SERVICE
    def add_service(self, service):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO SERVICE (TOWN, CAPACITY, CURRENT_PASSENGERS, LICENCE_PLATE, DEPARTURE_HOUR) VALUES (%s, %s, %s,%s,%s)"
            cursor.execute(query, (service.town, service.capacity, service.current_passengers, service.licence_plate,service.departure_hour))
            connection.commit()
            service_key = cursor.lastrowid
        return service_key

    def delete_service(self, service_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM SERVICE WHERE (ID = %s)"
            cursor.execute(query, (service_key,))
            connection.commit()

    def update_service(self, service_key, town, capacity, current_passengers, licence_plate, departure_hour):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE SERVICE SET TOWN = %s, CAPACITY = %s, CURRENT_PASSENGERS = %s, LICENCE_PLATE = %s, DEPARTURE_HOUR= %s WHERE (ID = %s)"
            cursor.execute(query, (service_key, town, capacity, current_passengers, licence_plate, departure_hour))
            connection.commit()
        return service_key
    
    def get_service(self, service_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT TOWN, CAPACITY, CURRENT_PASSENGERS, LICENCE_PLATE, DEPARTURE_HOUR FROM SERVICE WHERE (ID = %s)"
            cursor.execute(query, (service_key,))
            town,capacity,current_passengers,licence_plate,departure_hour = cursor.fetchone()
        service_ = Service(town,capacity,current_passengers,licence_plate,departure_hour)
        return service_
    
    def get_services(self):
        services = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, TOWN, CAPACITY, CURRENT_PASSENGERS, LICENCE_PLATE, DEPARTURE_HOUR FROM SERVICE ORDER BY ID"
            cursor.execute(query)
            for service_key,town,capacity,current_passengers,licence_plate,departure_hour in cursor:
                services.append((service_key, Service(town,capacity,current_passengers,licence_plate,departure_hour)))
        return services

#####WORKCHART
    def add_workchart(self, workchart):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO WORKCHART (PERSONID, JOBID, LEVELID, SALARY, FOOD_BUDGET, TOTAL_YEARS_WORKED, YEARS_IN_COMPANY, QUALIFIES_FOR_PENSION) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (workchart.personid, workchart.jobid, workchart.levelid, workchart.salary, workchart.foodbudget, workchart.total_yr_worked, workchart.yr_in_comp, workchart.qualify))
            connection.commit()
            workchart_key = workchart.personid
        return workchart_key

    def delete_workchart(self, workchart_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM WORKCHART WHERE (PERSONID = %s)"
            cursor.execute(query, (workchart_key,))
            connection.commit()

    def get_workchart(self, workchart_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT PERSONID, JOBID, LEVELID, SALARY, FOOD_BUDGET, TOTAL_YEARS_WORKED, YEARS_IN_COMPANY, QUALIFIES_FOR_PENSION FROM WORKCHART WHERE (PERSONID = %s)"
            cursor.execute(query, (workchart_key,))
            personid, jobid, levelid, salary, foodbudget, total_yr_worked, yr_in_comp, qualify = cursor.fetchone()
        workchart_ = Workchart(personid, jobid, levelid, salary, foodbudget, total_yr_worked, yr_in_comp, qualify)
        return workchart_

    def get_workcharts(self):
        workcharts = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT PERSONID, JOBID, LEVELID, SALARY, FOOD_BUDGET, TOTAL_YEARS_WORKED, YEARS_IN_COMPANY, QUALIFIES_FOR_PENSION FROM TRANSPORTATION ORDER BY SALARY DESC"
            cursor.execute(query)
            for personid, jobid, levelid, salary, foodbudget, total_yr_worked, yr_in_comp, qualify in cursor:
                workcharts.append((personid, Workchart(personid, jobid, levelid, salary, foodbudget, total_yr_worked, yr_in_comp, qualify)))
        return workcharts
#####TRANSPORTATION
    def add_transportation(self, transportation):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO TRANSPORTATION (PERSONID, SERVICEID, USES_IN_MORNING, USES_IN_EVENING, SEAT_NUMBER, SERVICE_FEE, STOP_NAME) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (transportation.personid, transportation.serviceid, transportation.uses_in_morning, transportation.uses_in_evening, transportation.seat_nr, transportation.service_fee, transportation.stop_name))
            connection.commit()
            transportation_key = transportation.personid
        return transportation_key

    def delete_transportation(self, transportation_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM TRANSPORTATION WHERE (PERSONID = %s)"
            cursor.execute(query, (transportation_key,))
            connection.commit()

    def get_transportation(self, transportation_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT PERSONID, SERVICEID, USES_IN_MORNING, USES_IN_EVENING, SEAT_NUMBER, SERVICE_FEE, STOP_NAME FROM TRANSPORTATION WHERE (PERSONID = %s)"
            cursor.execute(query, (transportation_key,))
            personid,serviceid, uses_in_morning, uses_in_evening, seat_nr, service_fee, stop_name = cursor.fetchone()
        transportation_ = Transportation(personid,serviceid, uses_in_morning, uses_in_evening, seat_nr, service_fee, stop_name)
        return transportation_

    def get_transportations(self):
        transportations = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT PERSONID, SERVICEID, USES_IN_MORNING, USES_IN_EVENING, SEAT_NUMBER, SERVICE_FEE, STOP_NAME FROM TRANSPORTATION ORDER BY SERVICEID"
            cursor.execute(query)
            for personid,serviceid, uses_in_morning, uses_in_evening, seat_nr, service_fee, stop_name in cursor:
                transportations.append((personid, Transportation(personid,serviceid, uses_in_morning, uses_in_evening, seat_nr, service_fee, stop_name)))
        return transportations