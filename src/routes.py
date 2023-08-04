# flask imports
from flask import request, jsonify, make_response, Blueprint
# Core application
from model import Account
from app import app, db
# Auth-related imports
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from auth import token_required
# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta

@token_required
def get_all_accounts(req):
    accounts = Account.query.all()
    output = []
    for account in accounts:
        output.append({
            'public_id': account.public_id,
            'name' : account.name,
            'email' : account.email
        })
    return jsonify({'accounts': output})

def login():
    auth = request.get_json()

    if not auth['email'] or not auth['password']:
        headers = {'WWW-Authenticate': 'Basic realm ="Login required"'}
        return make_response(
            'Could not verify', 401, headers
        )

    account = Account.query\
        .filter_by(email = auth['email'])\
        .first()

    if not account:
        headers = {'WWW-Authenticate': 'Basic realm ="Account does not exist"'}
        return make_response(
            'Could not verify', 401, headers
        )

    if check_password_hash(account.password, auth['password']):
        obj = {
            'public_id': account.public_id,
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
  
    # checking for existing account
    account = Account.query\
        .filter_by(email = email)\
        .first()
    if not account:
        # database ORM object
        account = Account(
            public_id = str(uuid.uuid4()),
            name = name,
            email = email,
            password = generate_password_hash(password)
        )
        # insert account
        db.session.add(account)
        db.session.commit()

        return make_response('Successfully registered.', 201)
    else:
        return make_response('This email is already registered to an account. Please Log in.', 202)
