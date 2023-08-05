# flask imports
from flask import request
# Core application
from model import Account
from app import app, db
# Schema
from flask_expects_json import expects_json
import schema
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
            'username': account.username,
            'email': account.email
        })
    res = {
        'accounts': output
    }
    return (res, 200)


@expects_json(schema.login)
def login():
    auth = request.get_json()
    account = Account.query\
        .filter_by(email = auth['email'])\
        .first()
    if not account:
        res = {
            'error': 'Please sign up.'
        }
        return (res, 401, {'WWW-Authenticate': 'Basic realm ="Account does not exist"'})

    if check_password_hash(account.password, auth['password']):
        token_data = {
            'public_id': account.public_id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }
        token = jwt.encode(token_data, app.config['SECRET_KEY'])
        res = {
            'token': token.decode('UTF-8')
        }
        return (res, 200)
    else:
        res = {
            'error': 'Could not verify'
        }
        return (res, 403, {'WWW-Authenticate': 'Basic realm ="Wrong Password"'})


@expects_json(schema.sign_up)
def signup():
    data = request.get_json()

    username, email = data['username'], data['email']
    password = data['password']
  
    # checking for existing account
    account = Account.query\
        .filter_by(email = email)\
        .first()
    if not account:
        # database ORM object
        account = Account(
            public_id = str(uuid.uuid4()),
            username = username,
            email = email,
            password = generate_password_hash(password)
        )
        # insert account
        db.session.add(account)
        db.session.commit()

        res = {
            'success': 'Successfully registered.'
        }
        return (res, 201)
    else:
        res = {
            'error': 'This email is already registered to an account. Please Log in.'
        }
        return (res, 202)
