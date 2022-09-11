from flask import Blueprint, request

from config.db import db
from models.Aid import Aid
from models.User import User


aids = Blueprint('aids', __name__)

@aids.route('/aids/<id>', methods = ['POST'])
def ayudas(id):

    get_user =  User.query.get(id)

    user = get_user.username
   
    latitude_user = request.json["latitude"]
    length_user = request.json["length"]
    type_aid = request.json["type_aid"]

    new_aid = Aid(user, latitude_user, length_user, type_aid)
    db.session.add(new_aid)
    db.session.commit()

    return {"status": "task saved"}


