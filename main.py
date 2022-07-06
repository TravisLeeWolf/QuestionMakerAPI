from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# Mock data
import mock_data

app = Flask(__name__)
Bootstrap(app)

data = mock_data.data
grade = [
    "Junior High Grade 1",
    "Junior High Grade 2",
    "Junior High Grade 3",
    "Elementary Grade 6",
    "Elementary Grade 5",
    "Elementary Grade 4",
    "Elementary Grade 3",
    "Elementary Grade 2",
    "Elementary Grade 1",
]

"""
Main page where list of questions are viewed
"""
@app.route("/")
def main_page():
    return render_template("index.html", grade=grade, data=data)


@app.route("/viewer")
def view():
    return render_template("viewer.html")


@app.route("/maker")
def make():
    return render_template("maker.html")


@app.route("/helper")
def helper():
    return render_template("api_helper.html")

if __name__ == "__main__":
    app.run(debug=True)