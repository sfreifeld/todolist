from app import db
from flask_sqlalchemy import SQLAlchemy


class toDo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    habit = db.Column(db.String(100), index=True)
    goal = db.Column(db.Integer, index=True)

    def __init__(self, habit, goal):
        self.habit = habit
        self.goal = goal
    
    def __repr__(self):
        return '<toDo %r >' % self.habit


