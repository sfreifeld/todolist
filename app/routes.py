from flask import Flask, render_template, request, abort, url_for, redirect, flash
from app import app
from app.models import toDo
from app import db
from flask_wtf import FlaskForm
from datetime import date
from app.forms import habitForm
from datetime import datetime, date, timedelta



@app.route('/', methods=['POST', 'GET']) 
def home():
    form = habitForm()
    if form.validate_on_submit():
        date = datetime.utcnow()
        habit = request.form['habit']
        goal = request.form['goal']
        record = toDo(habit, goal, date)
        db.session.add(record)
        db.session.commit()
    return render_template('index.html', form = form)
