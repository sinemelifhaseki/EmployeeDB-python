from datetime import datetime
from employee import Employee

from flask import current_app, render_template, request, redirect, url_for

def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)

def list_page():
    db = current_app.config["db"]
    if request.method == "GET":
        employees = db.get_employees()
        return render_template("listemployee.html", employees=sorted(employees))
    else:
        form_employee_keys = request.form.getlist("employee_keys")
        for form_employee_key in form_employee_keys:
            db.delete_employee(int(form_employee_key))
        return redirect(url_for("list_page"))

def employee_page(employee_key):
    db = current_app.config["db"]
    employee = db.get_employee(employee_key)
    if employee is None:
        abort(404)
    return render_template("employee.html", employee=employee)

def employee_add_page():
    if request.method == "GET":
        return render_template(
            "employee_edit.html", min_age=18, max_age=62
        )
    else:
        form_title = request.form["title"]
        form_age = request.form["age"]
        employee = Employee(form_title, age=int(form_age) if form_age else None)
        db = current_app.config["db"]
        employee_key = db.add_employee(employee)
        return redirect(url_for("employee_page", employee_key=employee_key))