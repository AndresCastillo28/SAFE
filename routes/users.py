from urllib import request
from flask import Blueprint, request

from config.db import db
from models.User import User


users = Blueprint('users', __name__)

@users.route('/users', methods = ['POST'])
def register_users():

    username = request.json["username"]
    password = request.json["password"]

    new_user = User(username, password)

    db.session.add(new_user)
    db.session.commit()

    return {"status": "User registered"}


