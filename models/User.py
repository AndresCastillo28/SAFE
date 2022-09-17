from config.db import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
 
    admin = db.Column(db.Boolean)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, admin, username, password):
    
        self.admin = admin
        self.username = username
        self.password = password