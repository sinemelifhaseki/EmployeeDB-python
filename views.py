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
    return render_template("employee.html", employee=employee)

def employee_add_page(): #add employee page
    if request.method == "GET":
        values = {"title": "", "age": ""}
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
        gender = request.form.data["gender"]
        height = request.form.data["height"]
        weight = request.form.data["weight"]
        employee = Employee(title, age, gender, height, weight)
        db = current_app.config["db"]
        employee_key = db.add_employee(employee)
        return redirect(url_for("employee_page", employee_key=employee_key))

def validate_employee_form(form):
    form.data = {}
    form.errors = {}

    form_title = form.get("title", "").strip()
    if len(form_title) == 0:
        form.errors["title"] = "Title cannot be blank!"
    else:
        form.data["title"] = form_title

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
        values = {"title": ""}
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
        is_executive = request.form.data["is_executive"]
        department = request.form.data["department"]
        is_active = request.form.data["is_active"]
        to_be_hired = request.form.data["to_be_hired"]
        jobtitle = Jobtitle(title, is_executive, department, is_active, to_be_hired)
        db = current_app.config["db"]
        jobtitle_key = db.add_jobtitle(jobtitle)
        return redirect(url_for("jobtitle_page", jobtitle_key=jobtitle_key))

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
        values = {"title": ""}
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
        experience = request.form.data["experience"]
        bonus_salary = request.form.data["bonus_salary"]
        is_director = request.form.data["is_director"]
        is_manager = request.form.data["is_manager"]
        level = Level(title, experience, bonus_salary, is_director, is_manager)
        db = current_app.config["db"]
        level_key = db.add_level(level)
        return redirect(url_for("level_page", level_key=level_key))

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
        values = {"town": ""}
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
        capacity = request.form.data["capacity"]
        current_passengers = request.form.data["current_passengers"]
        licence_plate = request.form.data["licence_plate"]
        departure_hour = request.form.data["departure_hour"]
        service = Service(town,capacity,current_passengers,licence_plate,departure_hour)
        db = current_app.config["db"]
        service_key = db.add_service(service)
        return redirect(url_for("service_page", service_key=service_key))

def validate_service_form(form):
    form.data = {}
    form.errors = {}

    form_title = form.get("town", "").strip()
    if len(form_title) == 0:
        form.errors["town"] = "Town cannot be blank!"
    else:
        form.data["town"] = form_title

    return len(form.errors) == 0

####

