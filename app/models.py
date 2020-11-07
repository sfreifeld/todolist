from app import db
from flask_sqlalchemy import SQLAlchemy


class toDo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    habit = db.Column(db.String(100))
    goal = db.Column(db.Integer)

    def __repr__(self):
        return '<toDo %r >' % self.habit