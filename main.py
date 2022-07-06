from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

"""
Main page where list of questions are viewed
"""
@app.route("/")
def main_page():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)