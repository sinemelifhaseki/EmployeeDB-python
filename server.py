from flask import Flask


app = Flask(__name__)


@app.route("/")
def home_page():
    return "Welcome to our project - itucsdb1916- Hakan&Sinem"


if __name__ == "__main__":
    app.run()
