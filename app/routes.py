from flask import Flask, render_template, request, abort, url_for, redirect
from app import app 
#from app.models import Todo 
from app import db 


@app.route('/') 
def home(): 
    return render_template('index.html') 


#@app.route('/add', methods=['POST']) 
# def add(): 
#    return redirect(url_for('index')) 