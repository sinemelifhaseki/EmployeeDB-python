from datetime import datetime

from flask import current_app, render_template

def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)

def list_page():
    db = current_app.config["db"]
    employees = db.get_employees()
    return render_template("listemployee.html", employees=sorted(employees))

def employee_page(movie_key):
    db = current_app.config["db"]
    employee = db.get_employee(employee_key)
    if employee is None:
        abort(404)
    return render_template("employee.html", employee=employee)