from config.db import db
from datetime import datetime

class Aid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100))
    latitude_user = db.Column(db.Float)
    length_user = db.Column(db.Float)
    type_aid = db.Column(db.String(100))
    date = db.Column(db.DateTime(100), default=datetime.utcnow)


    def __init__(self, user, latitude_user,length_user, type_aid):
        self.user = user
        self.latitude_user = latitude_user 
        self.length_user = length_user   
        self.type_aid = type_aid