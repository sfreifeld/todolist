from flask_wtf import FlaskForm 
from wtforms import StringField, TextField, IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length

class habitForm(FlaskForm):
    id = HiddenField()
    habit = StringField('habit', [
        DataRequired()])
    goal = IntegerField('goal', [
        DataRequired()])
    submit = SubmitField('submit')
