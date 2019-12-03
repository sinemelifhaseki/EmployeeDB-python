from datetime import datetime
from employee import Employee
from level import Level
from jobtitle import Jobtitle
from service import Service

from flask import current_app, render_template, request, redirect, url_for

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
        title = request.form.data["title"]
        age = request.form.data["age"]
        employee = Employee(title, age=age)
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
        jobtitle = Jobtitle(title)
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
        level = Level(title)
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