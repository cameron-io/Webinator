# flask imports
from flask import request
# Core application
from app import app
# Schema
from flask_expects_json import expects_json
import schema
# Auth-related imports
from werkzeug.security import check_password_hash
from auth import token_required
# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta
# DB layer
from db import get_user_by_email, query_all_accounts, create_user_account

@app.route('/accounts', methods = ['GET'])
@token_required
def get_all_accounts(_):
    accounts = query_all_accounts()
    res = {
        'accounts': accounts
    }
    return (res, 200)


@app.route('/login', methods = ['POST'])
@expects_json(schema.login)
def login():
    payload = request.get_json()
    account = get_user_by_email(payload['email'])
    if not account:
        res = {
            'error': 'Please sign up.'
        }
        return (res, 401, {'WWW-Authenticate': 'Basic realm ="Account does not exist"'})

    if check_password_hash(account.password, payload['password']):
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


@app.route('/signup', methods = ['POST'])
@expects_json(schema.sign_up)
def signup():
    data = request.get_json()
  
    # checking for existing account
    email = data['email']
    account = get_user_by_email(email)
    
    if not account:
        username = data['username']
        password = data['password']
        create_user_account(username, email, password)
        res = {
            'success': 'Successfully registered.'
        }
        return (res, 201)
    else:
        res = {
            'error': 'This email is already registered to an account. Please Log in.'
        }
        return (res, 202)
