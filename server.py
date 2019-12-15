import os
from flask_login import LoginManager
from datetime import datetime
from flask import Flask, render_template
import views
from user import get_user
from database import Database
from employee import Employee
from jobtitle import Jobtitle
from level import Level
from service import Service

lm = LoginManager()

@lm.user_loader
def load_user(user_id):
    return get_user(user_id)

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/login", view_func=views.login_page, methods=["GET", "POST"])
    app.add_url_rule("/logout", view_func=views.logout_page)
    
    app.add_url_rule("/employees", view_func=views.list_page, methods=["GET", "POST"])
    app.add_url_rule("/employees/<int:employee_key>", view_func=views.employee_page,methods=["GET", "POST"])
    app.add_url_rule("/employees/<int:employee_key>/edit", view_func=views.employee_update_page,methods=["GET", "POST"])
    app.add_url_rule("/new-employee", view_func=views.employee_add_page, methods=["GET", "POST"])

    app.add_url_rule("/jobtitles", view_func=views.list_jobtitles, methods=["GET", "POST"])
    app.add_url_rule("/jobtitles/<int:jobtitle_key>", view_func=views.jobtitle_page,methods=["GET", "POST"])
    app.add_url_rule("/jobtitles/<int:jobtitle_key>/edit", view_func=views.jobtitle_update_page,methods=["GET", "POST"])    
    app.add_url_rule("/new-jobtitle", view_func=views.jobtitle_add_page, methods=["GET", "POST"])

    app.add_url_rule("/levels", view_func=views.list_levels, methods=["GET", "POST"])
    app.add_url_rule("/levels/<int:level_key>", view_func=views.level_page,methods=["GET", "POST"])
    app.add_url_rule("/levels/<int:level_key>/edit", view_func=views.level_update_page,methods=["GET", "POST"])
    app.add_url_rule("/new-level", view_func=views.level_add_page, methods=["GET", "POST"])

    app.add_url_rule("/services", view_func=views.list_services, methods=["GET", "POST"])
    app.add_url_rule("/services/<int:service_key>", view_func=views.service_page, methods=["GET", "POST"])
    app.add_url_rule("/services/<int:service_key>/edit", view_func=views.service_update_page, methods=["GET", "POST"])
    app.add_url_rule("/new-service", view_func=views.service_add_page, methods=["GET", "POST"])

    app.add_url_rule("/workchart", view_func=views.list_workchart, methods=["GET", "POST"])
    app.add_url_rule("/workchart/<int:workchart_key>", view_func=views.workchart_page, methods=["GET", "POST"])
    app.add_url_rule("/workchart/<int:workchart_key>/edit", view_func=views.workchart_update_page, methods=["GET", "POST"])
    app.add_url_rule("/new-workchart", view_func=views.workchart_add_page, methods=["GET", "POST"])

    app.add_url_rule("/transportation", view_func=views.list_transportation, methods=["GET", "POST"])
    app.add_url_rule("/transportation/<int:transportation_key>", view_func=views.transportation_page, methods=["GET", "POST"])
    app.add_url_rule("/transportation/<int:transportation_key>/edit", view_func=views.transportation_update_page, methods=["GET", "POST"])
    app.add_url_rule("/new-transportation", view_func=views.transportation_add_page, methods=["GET", "POST"])

    lm.init_app(app)
    lm.login_view = "login_page"

    url = os.getenv("DATABASE_URL")
    db = Database(url)
    app.config["db"] = db


    return app

app=create_app()


if __name__ == "__main__":
    app.run()
