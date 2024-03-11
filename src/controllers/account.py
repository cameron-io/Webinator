# flask imports
from flask import request
# Core application
from app import app
# Schema
from flask_expects_json import expects_json
import validate.user as user
# Auth-related imports
from werkzeug.security import check_password_hash
from middleware.auth import token_required
# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta
# DB layer
from service.user import get_user_by_email, create_user_account


@app.route('/login', methods = ['POST'])
@expects_json(user.login)
def login():
    payload = request.get_json()
    account = get_user_by_email(payload['email'])
    if not account:
        res = {
            'error': 'Account not registered.'
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
        return ('', 200, {'set-cookie': f'token={token}; Path=/; HttpOnly; SameSite=strict;'})
    else:
        res = {
            'error': 'Could not verify'
        }
        return (res, 403, {'WWW-Authenticate': 'Basic realm ="Wrong Password"'})


@app.route('/register', methods = ['POST'])
@expects_json(user.register)
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
        return (res, 400)
