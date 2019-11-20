from datetime import datetime
from flask import Flask, render_template
import views
from database import Database
from employee import Employee


def create_app():
    app = Flask(__name__)
    #app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/employees", view_func=views.list_page, methods=["GET", "POST"])
    app.add_url_rule("/employees/<int:employee_key>", view_func=views.employee_page)
    app.add_url_rule("/new-employee", view_func=views.employee_add_page, methods=["GET", "POST"])

    db = Database()
    app.config["db"] = db


    return app

app=create_app()


if __name__ == "__main__":
    app.run()
