from datetime import datetime
from employee import Employee
from level import Level
from jobtitle import Jobtitle
from service import Service
from workchart import Workchart
from transportation import Transportation

from flask import abort, current_app, render_template, request, redirect, url_for

def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)

#############employee################

def list_page(): #show the employees
    db = current_app.config["db"]
    if request.method == "GET":
        employees = db.get_employees()
        return render_template("listemployee.html", employees=sorted(employees))
    else:
        form_employee_keys = request.form.getlist("employee_keys")
        for form_employee_key in form_employee_keys:
            db.delete_employee(int(form_employee_key))
        return redirect(url_for("list_page"))

def employee_page(employee_key): #show the key employee page
    db = current_app.config["db"]
    employee = db.get_employee(employee_key)
    if employee is None:
        abort(404)
    return render_template("employee.html", employee=employee, employee_key=employee_key)

def employee_add_page(): #add employee page
    if request.method == "GET":
        values = {"name": "", "age": "", "gender":"","height":"","weight":""}
        return render_template(
            "employee_edit.html", min_age=18, max_age=62,values=values,
        )
    else:
        valid = validate_employee_form(request.form)
        if not valid:
            return render_template(
            "employee_edit.html", min_age=18, max_age=62,values=request.form,
        )
        name = request.form.data["name"]
        age = request.form.data["age"]
        gender = request.form.get("gender")
        height = request.form.get("height")
        weight = request.form.get("weight")
        employee = Employee(name, age, gender, height, weight)
        db = current_app.config["db"]
        db.add_employee(employee)
        return redirect(url_for("list_page"))

def employee_update_page(employee_key):
    if request.method == "GET":
        values = {"name": "", "age": "", "gender":"","height":"","weight":""}
        return render_template(
            "employee_edit.html", min_age=18, max_age=62,values=values,employee_key=employee_key
        )
    else:
        valid = validate_employee_form(request.form)
        if not valid:
            return render_template(
            "employee_edit.html", min_age=18, max_age=62,values=request.form,employee_key=employee_key
        )
        name = request.form.data["name"]
        age = request.form.data["age"]
        gender = request.form.get("gender")
        height = request.form.get("height")
        weight = request.form.get("weight")
        #employee = Employee(name, age, gender, height, weight)
        db = current_app.config["db"]
        db.update_employee(employee_key, name, age, gender, height, weight)
        return redirect(url_for("list_page"))

def validate_employee_form(form):
    form.data = {}
    form.errors = {}

    form_title = form.get("name", "").strip()
    if len(form_title) == 0:
        form.errors["name"] = "Name cannot be blank!"
    else:
        form.data["name"] = form_title

    form_age = form.get("age")
    if not form_age:
        form.data["age"] = None
    elif not form_age.isdigit():
        form.errors["age"] = "Age must consist of digits only."
    else:
        age = int(form_age)
        if (age < 18) or (age > 62):
            form.errors["age"] = "Age not in valid range."
        else:
            form.data["age"] = age

    return len(form.errors) == 0

#########jobtitle########
def list_jobtitles(): #show the jobtitles
    db = current_app.config["db"]
    if request.method == "GET":
        jobtitles = db.get_jobtitles()
        return render_template("listjobtitle.html", jobtitles=sorted(jobtitles))
    else:
        form_jobtitle_keys = request.form.getlist("jobtitle_keys")
        for form_jobtitle_key in form_jobtitle_keys:
            db.delete_jobtitle(int(form_jobtitle_key))
        return redirect(url_for("list_jobtitles"))

def jobtitle_page(jobtitle_key): #show the key jobtitle page
    db = current_app.config["db"]
    jobtitle = db.get_jobtitle(jobtitle_key)
    if jobtitle is None:
        abort(404)
    return render_template("jobtitle.html", jobtitle=jobtitle, jobtitle_key=jobtitle_key)


def jobtitle_add_page(): #add jobtitle page
    if request.method == "GET":
        values = {"title": "", "is_executive": "","department": "","is_active": "","to_be_hired": ""}
        return render_template(
            "jobtitle_edit.html", values=values,
        )
    else:
        valid = validate_jobtitle_form(request.form)
        if not valid:
            return render_template(
            "jobtitle_edit.html",values=request.form,
        )
        title = request.form.data["title"]
        is_executive = request.form.get("is_executive")
        department = request.form.get("department")
        is_active = request.form.get("is_active")
        to_be_hired = request.form.get("to_be_hired")
        jobtitle = Jobtitle(title, is_executive, department, is_active, to_be_hired)
        db = current_app.config["db"]
        db.add_jobtitle(jobtitle)
        return redirect(url_for("list_jobtitles"))

def jobtitle_update_page(jobtitle_key): #edit jobtitle page
    if request.method == "GET":
        values = {"title": "", "is_executive": "","department": "","is_active": "","to_be_hired": ""}
        return render_template(
            "jobtitle_edit.html", values=values, jobtitle_key=jobtitle_key
        )
    else:
        valid = validate_jobtitle_form(request.form)
        if not valid:
            return render_template(
            "jobtitle_edit.html",values=request.form,jobtitle_key=jobtitle_key
        )
        title = request.form.data["title"]
        is_executive = request.form.get("is_executive")
        department = request.form.get("department")
        is_active = request.form.get("is_active")
        to_be_hired = request.form.get("to_be_hired")
        #jobtitle = Jobtitle(title, is_executive, department, is_active, to_be_hired)
        db = current_app.config["db"]
        db.update_jobtitle(jobtitle_key, title, is_executive, department, is_active, to_be_hired)
        return redirect(url_for("list_jobtitles"))

def validate_jobtitle_form(form):
    form.data = {}
    form.errors = {}

    form_title = form.get("title", "").strip()
    if len(form_title) == 0:
        form.errors["title"] = "Title cannot be blank!"
    else:
        form.data["title"] = form_title

    return len(form.errors) == 0

###########level###############

def list_levels(): #show the levels
    db = current_app.config["db"]
    if request.method == "GET":
        levels = db.get_levels()
        return render_template("listlevel.html", levels=sorted(levels))
    else:
        form_level_keys = request.form.getlist("level_keys")
        for form_level_key in form_level_keys:
            db.delete_level(int(form_level_key))
        return redirect(url_for("list_levels"))

def level_page(level_key): #show the key level page
    db = current_app.config["db"]
    level = db.get_level(level_key)
    if level is None:
        abort(404)
    return render_template("level.html", level=level,level_key=level_key)


def level_add_page(): #add level page
    if request.method == "GET":
        values = {"title": "","experience": "","bonus_salary": "","is_director": "","is_manager": ""}
        return render_template(
            "level_edit.html", values=values,
        )
    else:
        valid = validate_level_form(request.form)
        if not valid:
            return render_template(
            "level_edit.html",values=request.form,
        )
        title = request.form.data["title"]
        experience = request.form.get("experience")
        bonus_salary = request.form.get("bonus_salary")
        is_director = request.form.get("is_director")
        is_manager = request.form.get("is_manager")
        level = Level(title, experience, bonus_salary, is_director, is_manager)
        db = current_app.config["db"]
        db.add_level(level)
        return redirect(url_for("list_levels"))

def level_update_page(level_key): #edit level page
    if request.method == "GET":
        values = {"title": "","experience": "","bonus_salary": "","is_director": "","is_manager": ""}
        return render_template(
            "level_edit.html", values=values,level_key=level_key
        )
    else:
        valid = validate_level_form(request.form)
        if not valid:
            return render_template(
            "level_edit.html",values=request.form,level_key=level_key
        )
        title = request.form.data["title"]
        experience = request.form.get("experience")
        bonus_salary = request.form.get("bonus_salary")
        is_director = request.form.get("is_director")
        is_manager = request.form.get("is_manager")
        #level = Level(title, experience, bonus_salary, is_director, is_manager)
        db = current_app.config["db"]
        db.update_level(level_key, title, experience, bonus_salary, is_director, is_manager)
        return redirect(url_for("list_levels"))

def validate_level_form(form):
    form.data = {}
    form.errors = {}

    form_title = form.get("title", "").strip()
    if len(form_title) == 0:
        form.errors["title"] = "Title cannot be blank!"
    else:
        form.data["title"] = form_title

    return len(form.errors) == 0

########service########
def list_services(): #show the services
    db = current_app.config["db"]
    if request.method == "GET":
        services = db.get_services()
        return render_template("listservice.html", services=sorted(services))
    else:
        form_service_keys = request.form.getlist("service_keys")
        for form_service_key in form_service_keys:
            db.delete_service(int(form_service_key))
        return redirect(url_for("list_services"))

def service_page(service_key): #show the key service page
    db = current_app.config["db"]
    service = db.get_service(service_key)
    if service is None:
        abort(404)
    return render_template("service.html", service=service,service_key=service_key)


def service_add_page(): #add service page
    if request.method == "GET":
        values = {"town": "","capacity": "","current_passengers": "","licence_plate": "","departure_hour": ""}
        return render_template(
            "service_edit.html", values=values,
        )
    else:
        valid = validate_service_form(request.form)
        if not valid:
            return render_template(
            "service_edit.html",values=request.form,
        )
        town = request.form.data["town"]
        capacity = request.form.get("capacity")
        current_passengers = request.form.get("current_passengers")
        licence_plate = request.form.get("licence_plate")
        departure_hour = request.form.get("departure_hour")
        service = Service(town,capacity,current_passengers,licence_plate,departure_hour)
        db = current_app.config["db"]
        db.add_service(service)
        return redirect(url_for("list_services"))

def service_update_page(service_key): #edit service page
    if request.method == "GET":
        values = {"town": "","capacity": "","current_passengers": "","licence_plate": "","departure_hour": ""}
        return render_template(
            "service_edit.html", values=values,service_key=service_key
        )
    else:
        valid = validate_service_form(request.form)
        if not valid:
            return render_template(
            "service_edit.html",values=request.form,service_key=service_key
        )
        town = request.form.data["town"]
        capacity = request.form.get("capacity")
        current_passengers = request.form.get("current_passengers")
        licence_plate = request.form.get("licence_plate")
        departure_hour = request.form.get("departure_hour")
        #service = Service(town,capacity,current_passengers,licence_plate,departure_hour)
        db = current_app.config["db"]
        db.update_service(service_key, town, capacity, current_passengers, licence_plate, departure_hour)
        return redirect(url_for("list_services"))

def validate_service_form(form):
    form.data = {}
    form.errors = {}

    form_title = form.get("town", "").strip()
    if len(form_title) == 0:
        form.errors["town"] = "Town cannot be blank!"
    else:
        form.data["town"] = form_title

    return len(form.errors) == 0

#######workchart######
def list_workchart(): #show the workchart
    db = current_app.config["db"]
    if request.method == "GET":
        personlist = []
        workchart = db.get_workcharts()
        for personid ,work in workchart:
            person = db.get_employee(personid) 
            job = db.get_jobtitle(work.jobid)
            workchart_key = personid
            personlist.append((workchart_key, person.name, job.title))
        return render_template("listworkchart.html", personlist=personlist)
    else:
        form_workchart_keys = request.form.getlist("workchart_keys")
        for form_workchart_key in form_workchart_keys:
            db.delete_workchart(int(form_workchart_key))
        return redirect(url_for("list_workchart"))

def workchart_page(workchart_key): #show the key workchart page
    db = current_app.config["db"]
    workchart = db.get_workchart(workchart_key)
    person = db.get_employee(workchart.personid) 
    job = db.get_jobtitle(workchart.jobid)
    level = db.get_level(workchart.levelid)
    if workchart is None:
        abort(404)
    return render_template("workchart.html", name=person.name, jobtitle=job.title, levelname=level.title, salary=workchart.salary, foodbudget=workchart.foodbudget,total_yr_worked=workchart.total_yr_worked,yr_in_comp=workchart.yr_in_comp,qualify=workchart.qualify, workchart_key=workchart_key)

def workchart_add_page(): #add workchart page
    db = current_app.config["db"]
    if request.method == "GET":
        values = {"name": "","jobtitle": "","levelname": "","salary": "","foodbudget": "", "total_yr_worked":"", "yr_in_comp":"", "qualify":""}
        peoplenames = []
        people = db.get_employees()
        for employee_key, person in people:
                peoplenames.append((person.name))
        jobnames = []
        jobs = db.get_jobtitles()
        for jobtitle_key, job in jobs:
                jobnames.append((job.title))
        levelnames = []
        levels = db.get_levels()
        for level_key, lev in levels:
                levelnames.append((lev.title))
        return render_template(
            "workchart_edit.html", values=values, peoplenames = peoplenames, jobnames = jobnames, levelnames = levelnames
        )
    else:
        valid = validate_workchart_form(request.form)
        if not valid:
            return render_template(
            "workchart_edit.html",values=request.form,
        )
        name = request.form.get("name")
        personid = db.get_employee_id(name)
        jobtitle = request.form.get("jobtitle")
        jobid = db.get_jobtitle_id(jobtitle)
        levelname = request.form.get("levelname")
        levelid = db.get_level_id(levelname)
        salary = request.form.data["salary"]
        foodbudget = request.form.get("foodbudget")
        total_yr_worked = request.form.get("total_yr_worked")
        yr_in_comp = request.form.get("yr_in_comp")
        qualify = request.form.get("qualify")
        workchart = Workchart(personid, jobid, levelid, salary, foodbudget, total_yr_worked, yr_in_comp, qualify)
        db = current_app.config["db"]
        db.add_workchart(workchart)
        return redirect(url_for("list_workchart"))

def workchart_update_page(workchart_key): #update workchart page
    db = current_app.config["db"]
    if request.method == "GET":
        values = {"name": "","jobtitle": "","levelname": "","salary": "","foodbudget": "", "total_yr_worked":"", "yr_in_comp":"", "qualify":""}
        peoplenames = []
        people = db.get_employees()
        for employee_key, person in people:
                peoplenames.append((person.name))
        jobnames = []
        jobs = db.get_jobtitles()
        for jobtitle_key, job in jobs:
                jobnames.append((job.title))
        levelnames = []
        levels = db.get_levels()
        for level_key, lev in levels:
                levelnames.append((lev.title))
        return render_template(
            "workchart_edit.html", values=values, peoplenames = peoplenames, jobnames = jobnames, levelnames = levelnames, workchart_key=workchart_key
        )
    else:
        valid = validate_workchart_form(request.form)
        if not valid:
            return render_template(
            "workchart_edit.html",values=request.form, workchart_key=workchart_key
        )
        name = request.form.get("name")
        personid = db.get_employee_id(name)
        jobtitle = request.form.get("jobtitle")
        jobid = db.get_jobtitle_id(jobtitle)
        levelname = request.form.get("levelname")
        levelid = db.get_level_id(levelname)
        salary = request.form.data["salary"]
        foodbudget = request.form.get("foodbudget")
        total_yr_worked = request.form.get("total_yr_worked")
        yr_in_comp = request.form.get("yr_in_comp")
        qualify = request.form.get("qualify")
        #workchart = Workchart(personid, jobid, levelid, salary, foodbudget, total_yr_worked, yr_in_comp, qualify)
        db = current_app.config["db"]
        db.update_workchart(personid, jobid, levelid, salary, foodbudget, total_yr_worked, yr_in_comp, qualify)
        return redirect(url_for("list_workchart"))

def validate_workchart_form(form):
    form.data = {}
    form.errors = {}

    form_salary = form.get("salary")
    if not form_salary.isdigit():
        form.errors["salary"] = "Salary must consist of digits only."
    else:
        salary = int(form_salary)
        form.data["salary"] = salary

    return len(form.errors) == 0




######transportation#####
def list_transportation(): #show the transportation
    db = current_app.config["db"]
    if request.method == "GET":
        personlist = []
        transportation = db.get_transportations()
        for personid ,transport in transportation:
            person = db.get_employee(personid) 
            service = db.get_service(transport.serviceid)
            transportation_key = personid
            personlist.append((transportation_key, person.name, service.town))
        return render_template("listtransportation.html", personlist=personlist)
    else:
        form_transportation_keys = request.form.getlist("transportation_keys")
        for form_transportation_key in form_transportation_keys:
            db.delete_transportation(int(form_transportation_key))
        return redirect(url_for("list_transportation"))

def transportation_page(transportation_key): #show the key transportation page
    db = current_app.config["db"]
    transportation = db.get_transportation(transportation_key)
    person = db.get_employee(transportation.personid) 
    service = db.get_service(transportation.serviceid)
    if transportation is None:
        abort(404)
    return render_template("transportation.html", name=person.name, town=service.town, uses_in_morning=transportation.uses_in_morning, uses_in_evening=transportation.uses_in_morning, seat_nr=transportation.seat_nr, service_fee=transportation.service_fee, stop_name=transportation.stop_name, transportation_key=transportation_key)

def transportation_add_page(): #add transportation page
    db = current_app.config["db"]
    if request.method == "GET":
        values = {"name": "","town": "","uses_in_morning": "","uses_in_evening": "","seat_nr": "", "service_fee":"", "stop_name":""}
        peoplenames = []
        people = db.get_employees()
        for employee_key, person in people:
                peoplenames.append((person.name))
        towns = []
        services = db.get_services()
        for service_key, serv in services:
                towns.append((serv.town))        
        return render_template(
            "transportation_edit.html", values=values, peoplenames = peoplenames, towns = towns
        )
    else:
        valid = validate_transportation_form(request.form)
        if not valid:
            return render_template(
            "transportation_edit.html",values=request.form,
        )
        name = request.form.get("name")
        personid = db.get_employee_id(name)
        town = request.form.get("town")
        serviceid = db.get_service_id(town)
        uses_in_morning = request.form.get("uses_in_morning")
        uses_in_evening = request.form.get("uses_in_evening")
        seat_nr = request.form.data["seat_nr"]
        service_fee = request.form.data["service_fee"]
        stop_name = request.form.get("stop_name")
        transportation = Transportation(personid, serviceid, uses_in_morning, uses_in_evening, seat_nr, service_fee, stop_name)
        db = current_app.config["db"]
        db.add_transportation(transportation)
        return redirect(url_for("list_transportation"))

def transportation_update_page(transportation_key): #update workchart page
    db = current_app.config["db"]
    if request.method == "GET":
        values = {"name": "","town": "","uses_in_morning": "","uses_in_evening": "","seat_nr": "", "service_fee":"", "stop_name":""}
        peoplenames = []
        people = db.get_employees()
        for employee_key, person in people:
                peoplenames.append((person.name))
        towns = []
        services = db.get_services()
        for service_key, serv in services:
                towns.append((serv.town))
        return render_template(
            "transportation_edit.html", values=values, peoplenames = peoplenames, towns = towns, transportation_key=transportation_key
        )
    else:
        valid = validate_transportation_form(request.form)
        if not valid:
            return render_template(
            "transportation_edit.html",values=request.form, transportation_key=transportatiton_key
        )
        name = request.form.get("name")
        personid = db.get_employee_id(name)
        town = request.form.get("town")
        serviceid = db.get_service_id(town)
        uses_in_morning = request.form.get("uses_in_morning")
        uses_in_evening = request.form.get("uses_in_evening")
        seat_nr = request.form.data["seat_nr"]
        service_fee = request.form.data["service_fee"]
        stop_name = request.form.get("stop_name")
        db = current_app.config["db"]
        db.update_transportation(personid, serviceid, uses_in_morning, uses_in_evening, seat_nr, service_fee, stop_name)
        return redirect(url_for("list_transportation"))

def validate_transportation_form(form):
    form.data = {}
    form.errors = {}

    form_seat = form.get("seat_nr")
    if not form_seat.isdigit():
        form.errors["seat_nr"] = "Seat number must consist of digits only."
    else:
        seat_nr = int(form_seat)
        form.data["seat_nr"] = seat_nr

    form_fee = form.get("service_fee")
    if not form_fee.isdigit():
        form.errors["service_fee"] = "Service fee must consist of digits only."
    else:
        service_fee = int(form_fee)
        form.data["service_fee"] = service_fee


    return len(form.errors) == 0