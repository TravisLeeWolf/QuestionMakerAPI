from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('template/index.html')


@app.route("/view")
def view():
    return render_template('template/questionViewer.html')


@app.route("/make")
def make():
    return render_template('template/questionMaker.html')

@app.route("/helper")
def helper():
    return render_template('template/apiHelper')


if __name__ == "__main__":
    app.run()