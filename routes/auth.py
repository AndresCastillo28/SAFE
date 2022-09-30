from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash

import jwt
import datetime

from models.User import User
from config.config import SECRET_KEY


auth = Blueprint('auth', __name__)


@auth.route('/login', methods = ['POST'])
def login_user():

    user_auth = request.json['email']
    password_auth = request.json['password']


    if not user_auth: 
        return jsonify({'message': 'Ingrese un username valido'}), 401
    if not password_auth:
        return({'message': 'Ingrese una contraseña valida'}), 401

    user = User.query.filter_by(email=user_auth).first()

    if not user:
        return jsonify({'message': 'User not found'}), 401  
    
    password = user.password
    
    if(check_password_hash(password, password_auth)):
        token = jwt.encode({'id': user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY, algorithm='HS256')
        return jsonify({'token' : token}), 200

    return jsonify({'message': 'Login is required'}), 401

