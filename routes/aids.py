from flask import Blueprint, request

from config.db import db
from models.Aid import Aid


aids = Blueprint('aids', __name__)

@aids.route('/aids', methods = ['POST'])
def register_users():

    username = request.json["username"]
    password = request.json["password"]

    new_aid = Aid(username, password)

    db.session.add(new_aid)
    db.session.commit()

    return {"status": "Aid registered"}


