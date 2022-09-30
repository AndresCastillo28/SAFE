from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

from config.db import db
from models.User import User

users = Blueprint('users', __name__)


@users.route('/users', methods = ['POST'])
def register_users():

    email = request.json["email"]
    cedula = request.json["cedula"]

    if not email: return jsonify({ 'ok': 'false', 'message': 'Ingrese email' })
    if not cedula: return jsonify({ 'ok': 'false', 'message': 'Ingrese cedula' })


    if (not '@' in email):
        return jsonify({
            "ok": "false",
            "message": "No es un correo valido"
        }), 400
    
    if (not cedula.isnumeric()):
        return jsonify({
            "ok": "false",
            "message": "Cédula invalida"
        }), 400

    # cedula = int(cedula)
    if (len(cedula) < 10 ):
        return jsonify({
            'ok': 'false',
            'message': 'cedula invalida'
        }), 400
    if (len(cedula) > 10):
        return jsonify({ 'ok': 'false', 'message' : 'cedula invalida' }), 400

    user = User.query.filter_by(email=email).first()
    user_cedula = User.query.filter_by(cedula=cedula).first()

    if(user_cedula): return jsonify({ 'ok': 'false', 'message': 'Ya existe un usuario con esa cédula' }), 400

    if(user): 
        return jsonify({
            "ok": "false",
            "message": "Ya existe un usuario con ese correo"
        }), 400

    password = request.json["password"]

    if not password: return jsonify({ 'ok': 'false', 'message': 'Ingrese una contraseña' }), 400
    if(len(password) < 6):
        return jsonify({
            'ok': 'false',
            'message': 'La contraseña debe tener 6 caracteres o más'
        }), 400

    new_password = generate_password_hash(password, method='pbkdf2:sha1', salt_length=8)

    new_user = User(email, cedula, new_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "ok": "true",
        "message": "User registered"
    })


  

