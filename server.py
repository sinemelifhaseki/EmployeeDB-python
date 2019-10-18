from datetime import datetime
from flask import Flask, render_template
import views
from database import Database
from employee import Employee

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    #app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/listemployee", view_func=views.list_page)

    db = Database()
    db.add_employee(Employee("Sinem Elif Haseki", age=22))
    db.add_employee(Employee("Hakan Sarac"))
    app.config["db"] = db


    return app



if __name__ == "__main__":
    app=create_app()
    app.run()
