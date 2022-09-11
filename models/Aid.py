from config.db import db
from datetime import datetime

class Aid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100))
    date = db.Column(db.DateTime(100), default=datetime.utcnow)
    location = db.Column(db.String(100))
    type_aid = db.Column(db.String(100))

    def __init__(self, user, date, location, type_aid):
        self.username = user
        self.password = date,
        self.location = location
        self.type_aid = type_aid    