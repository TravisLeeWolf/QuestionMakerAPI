from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField, widgets
from wtforms.validators import DataRequired, URL

# From doobeh on GitHub
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

# New question form
class create_question(FlaskForm):
    en_text = StringField(label="Question Text", validators=[DataRequired()])
    ja_text = StringField(label="Japanese Translation (Optional)")
    hint_text = StringField(label="Hint (Optional)")
    pic_url = StringField(label="Image URL", validators=[DataRequired(), URL()])
    tags = StringField(label="Tags (Separate tags with a comma)", validators=[DataRequired()])
    grades = MultiCheckboxField(label="Grades", validators=[DataRequired()], choices=[
        ("1", "ES 1st"),
        ("2", "ES 2nd"),
        ("3", "ES 3rd"),
        ("4", "ES 4th"),
        ("5", "ES 5th"),
        ("6", "ES 6th"),
        ("7", "JHS 1st"),
        ("8", "JHS 2nd"),
        ("9", "JHS 3rd"),
    ])
    submit = SubmitField("Add new question")
