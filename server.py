from flask import Flask


app = Flask(__name__)


@app.route("/")
def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)

@app.route("/addemployee")
def movies_page():
    return render_template("addemployee.html")


if __name__ == "__main__":
    app.run()
