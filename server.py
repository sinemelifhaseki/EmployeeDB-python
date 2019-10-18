from datetime import datetime
from flask import Flask, render_template
import views

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    #app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/addemployee", view_func=views.add_page)

    return app



if __name__ == "__main__":
    app=create_app()
    app.run()
