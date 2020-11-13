from flask_wtf import FlaskForm 
from wtforms import StringField, TextField, IntegerField, SubmitField, HiddenField, DateTimeField, DateField
from wtforms.validators import DataRequired, Length

class habitForm(FlaskForm):
    id = HiddenField()
    habit = StringField('habit', [
        DataRequired()])
    goal = IntegerField('goal', [
        DataRequired()])
    date = HiddenField('date')
    submit = SubmitField('submit')
