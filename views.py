from datetime import datetime
from employee import Employee
from level import Level
from jobtitle import Jobtitle
from service import Service

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
    return render_template("jobtitle.html", jobtitle=jobtitle)


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
    return render_template("level.html", level=level)


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
    return render_template("service.html", service=service)


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
        workchart = db.get_workchart()
        return render_template("listworkchart.html", workchart = sorted(workchart))
    else:
        form_workchart_keys = request.form.getlist("workchart_keys")
        for form_workchart_key in form_workchart_keys:
            db.delete_workchart(int(form_workchart_key))
        return redirect(url_for("list_workchart"))

def workchart_page(workchart_key): #show the key workchart page
    db = current_app.config["db"]
    workchart = db.get_workchart(workchart_key)
    if workchart is None:
        abort(404)
    return render_template("workchart.html", workchart=workchart)

###############BURDAYIM
def workchart_add_page(): #add workchart page
    if request.method == "GET":
        db = current_app.config["db"]
        values = {"personid": "","jobid": "","levelid": "","salary": "","foodbudget": "", "total_yr_worked":"", "yr_in_comp":"", "qualify":""}
        peoplenames = []
        people = db.get_employees()
        for employee_key, name, age, gender, height, weight in people:
                peoplenames.append((name))
        jobnames = []
        jobs = db.get_jobtitles()
        for jobtitle_key, title, is_executive, department, is_active, to_be_hired in jobs:
                jobnames.append((title))
        levelnames = []
        levels = db.get_levels()
        for level_key, title, experience, bonus_salary, is_director, is_manager in levels:
                levelnames.append((title))
        return render_template(
            "workchart_edit.html", values=values, peoplenames = peoplenames, jobnames = jobnames, levelnames = levelnames
        )
    else:
        valid = validate_workchart_form(request.form)
        if not valid:
            return render_template(
            "workchart_edit.html",values=request.form,
        )
        personid = request.form.data["personid"]
        capacity = request.form.get("capacity")
        current_passengers = request.form.get("current_passengers")
        licence_plate = request.form.get("licence_plate")
        departure_hour = request.form.get("departure_hour")
        service = Service(town,capacity,current_passengers,licence_plate,departure_hour)
        db = current_app.config["db"]
        db.add_service(service)
        return redirect(url_for("list_services"))






######transportation#####


