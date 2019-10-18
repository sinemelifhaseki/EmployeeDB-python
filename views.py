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