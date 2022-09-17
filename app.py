from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


from config.db import db
from routes.users import users
from routes.aids import aids
from routes.auth import auth
from config.config import DATABASE_CONNECTION_URI
from config.config import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)
CORS(app)

@app.route('/')
def index():
    return {'status': 'API running'}
    
with app.app_context():
    db.create_all()

app.register_blueprint(aids)
app.register_blueprint(users)
app.register_blueprint(auth)


if __name__ == '__main__':
    app.run(debug = True)   