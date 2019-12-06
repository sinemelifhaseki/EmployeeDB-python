import os
from datetime import datetime
from flask import Flask, render_template
import views
from database import Database
from employee import Employee
from jobtitle import Jobtitle
from level import Level
from service import Service


def create_app():
    app = Flask(__name__)
    #app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/employees", view_func=views.list_page, methods=["GET", "POST"])
    app.add_url_rule("/employees/<int:employee_key>", view_func=views.employee_page)
    app.add_url_rule("/new-employee", view_func=views.employee_add_page, methods=["GET", "POST"])

    app.add_url_rule("/jobtitles", view_func=views.list_jobtitles, methods=["GET", "POST"])
    app.add_url_rule("/jobtitles/<int:jobtitle_key>", view_func=views.jobtitle_page)
    app.add_url_rule("/new-jobtitle", view_func=views.jobtitle_add_page, methods=["GET", "POST"])

    app.add_url_rule("/levels", view_func=views.list_levels, methods=["GET", "POST"])
    app.add_url_rule("/levels/<int:level_key>", view_func=views.level_page)
    app.add_url_rule("/new-level", view_func=views.level_add_page, methods=["GET", "POST"])

    app.add_url_rule("/services", view_func=views.list_services, methods=["GET", "POST"])
    app.add_url_rule("/services/<int:service_key>", view_func=views.service_page)
    app.add_url_rule("/new-service", view_func=views.service_add_page, methods=["GET", "POST"])

    url = os.getenv("DATABASE_URL")
    db = Database(url)
    app.config["db"] = db


    return app

app=create_app()


if __name__ == "__main__":
    app.run()
