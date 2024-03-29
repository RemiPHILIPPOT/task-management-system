from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    task_name = StringField('Task Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
