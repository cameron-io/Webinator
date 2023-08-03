# flask imports
from flask import request, jsonify, make_response, Blueprint
# Core application
from model import User
from app import app, db
# Auth-related imports
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from auth import token_required
# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta

@token_required
def get_all_users(req):
    users = User.query.all()
    output = []
    for user in users:
        output.append({
            'public_id': user.public_id,
            'name' : user.name,
            'email' : user.email
        })
    return jsonify({'users': output})

def login():
    auth = request.get_json()

    if not auth['email'] or not auth['password']:
        headers = {'WWW-Authenticate': 'Basic realm ="Login required"'}
        return make_response(
            'Could not verify', 401, headers
        )

    user = User.query\
        .filter_by(email = auth['email'])\
        .first()

    if not user:
        headers = {'WWW-Authenticate': 'Basic realm ="User does not exist"'}
        return make_response(
            'Could not verify', 401, headers
        )

    if check_password_hash(user.password, auth['password']):
        obj = {
            'public_id': user.public_id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }
        token = jwt.encode(obj, app.config['SECRET_KEY'])
        return make_response(jsonify({'token': token.decode('UTF-8')}), 200)
    else:
        headers = {'WWW-Authenticate': 'Basic realm ="Wrong Password"'}
        return make_response(
            'Could not verify', 403, headers
        )

def signup():
    data = request.get_json()

    name, email = data['name'], data['email']
    password = data['password']
  
    # checking for existing user
    user = User.query\
        .filter_by(email = email)\
        .first()
    if not user:
        # database ORM object
        user = User(
            public_id = str(uuid.uuid4()),
            name = name,
            email = email,
            password = generate_password_hash(password)
        )
        # insert user
        db.session.add(user)
        db.session.commit()

        return make_response('Successfully registered.', 201)
    else:
        return make_response('This email is already registered to an account. Please Log in.', 202)
