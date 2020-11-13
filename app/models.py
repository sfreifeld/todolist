from app import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


class toDo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    habit = db.Column(db.String(100), index=True)
    goal = db.Column(db.Integer, index=True)
    date = db.Column(db.DateTime(timezone=True),index=True)

    def __init__(self, habit, goal, date):
        self.habit = habit
        self.goal = goal
        self.date = date
    
    def __repr__(self):
        return '<toDo %r >' % self.habit


