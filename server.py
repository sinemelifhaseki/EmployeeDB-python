from flask import Flask


app = Flask(__name__)


@app.route("/")
def home_page():
    return "Welcome to our project - itucsdb1916"


if __name__ == "__main__":
    app.run()
