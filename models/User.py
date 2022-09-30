from config.db import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    cedula = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, email, cedula ,password):
    
        self.email = email
        self.cedula = cedula
        self.password = password