from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false
from forms import create_question
# Mock data
import mock_data

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
Bootstrap(app)

# Database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

# Database for questions
class Questions(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    en_text = db.Column(db.String, nullable=False)
    ja_text = db.Column(db.String)
    pic_url = db.Column(db.String, nullable=False)
    hint_text = db.Column(db.String)
    grades = db.Column(db.String, nullable=False)
    tags = db.Column(db.String, nullable=False)
db.create_all()

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
    questions = Questions.query.all()

    return render_template("index.html", grade=grade, questions=questions)


@app.route("/viewer")
def view():
    return render_template("viewer.html")


@app.route("/maker", methods=["GET", "POST"])
def maker():
    form = create_question()
    if form.validate_on_submit():
        grades = ""
        for grade in form.grades.data:
            grades += (grade + ",")
        new_question = Questions(
            en_text = form.en_text.data,
            ja_text  = form.ja_text.data,
            pic_url = form.pic_url.data,
            hint_text = form.hint_text.data,   
            grades = grades,
            tags = form.tags.data,
        )
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for("main_page"))

    return render_template("maker.html", form=form)


@app.route("/helper")
def helper():
    return render_template("api_helper.html")

if __name__ == "__main__":
    app.run(debug=True)