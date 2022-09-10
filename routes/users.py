from flask import Blueprint

users = Blueprint('users', __name__)

@users.route('/users')
def register_users():
    return 'register user route'

