from flask import Flask, render_template, request, abort, url_for, redirect
from app import app
from app.models import toDo
from app import db


@app.route('/') 
def home(): 
    return render_template('index.html') 

@app.route('/todo', methods=['POST', 'GET']) 
def submitToDo():
    if request.method == 'POST':
        habit = request.form['habit']
        goal = request.form['goal']
        db.session.add(habit)
        db.session.commit()
        db.session.add(goal)
        db.session.commit()
        return render_template('index.html', habit = habit, goal = goal)
    else:
        return 'bye'
