from flask import Blueprint, request, jsonify

from config.db import db
from models.Aid import Aid, aids_schema
from models.User import User
from utils.token import token_required

aids = Blueprint('aids', __name__)

#Create a new assistance for especific user
@aids.route('/aids/<id>', methods = ['POST'])
def ask_assistance(id):

    get_user =  User.query.get(id)
 
    user = get_user.username
   
    latitude_user = request.json["latitude"]
    longitude_user = request.json["longitude"]
    type_aid = request.json["type_aid"]

    new_aid = Aid(user, latitude_user, longitude_user, type_aid)
    db.session.add(new_aid)
    db.session.commit()

    return {"status": "task saved"}


#Get assistance by id
@aids.route('/aids/<id>', methods = ['GET'])
@token_required
def get_assistance(current_user, id):

    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    user_assistance = Aid.query.get(id)

    user = user_assistance.user
    user_latitude = user_assistance.latitude_user
    user_longitude = user_assistance.longitude_user
    date = user_assistance.date

    return ({
        "user": user,
        "latitude": user_latitude,
        "longitude": user_longitude,
        "date": date
    })


#Get all assistances
@aids.route('/aids', methods = ['GET'])
@token_required
def get_assistances(current_user):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    aids = Aid.query.all()
    result = aids_schema.dump(aids)
    
    return jsonify(result)
