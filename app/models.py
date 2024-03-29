from datetime import datetime
from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(20), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Task('{self.title}', '{self.priority}', '{self.due_date}')"
