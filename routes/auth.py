from flask import Blueprint, request, jsonify
import jwt
import datetime

from models.User import User
from config.config import SECRET_KEY


auth = Blueprint('auth', __name__)


@auth.route('/login', methods = ['POST'])
def login_user():

    user_auth = request.json['username']
    password_auth = request.json['password']

    if not user_auth: 
        return jsonify({'message': 'Ingrese un username valido'}), 401
    if not password_auth:
        return({'message': 'Ingrese una contraseña valida'}), 401

    user = User.query.filter_by(username=user_auth).first()
    print(user.admin)
    
    if not user:
        return jsonify({'message': 'User not found'}), 401
    
    
    if(password_auth == user.password):
        token = jwt.encode({'id': user.id, 'admin': user.admin, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY, algorithm='HS256')
        return jsonify({'token' : token}), 200

    return jsonify({'message': 'Login is required'}), 401

