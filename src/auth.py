from flask import request
from functools import wraps
import jwt
from app import app
from db import get_user_by_public_id

# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token()
        if token == None:
            return ('', 401)
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            account_data = get_user_by_public_id(data['public_id'])
        except:
            return ('', 403)
        # returns the current logged in account's context to the routes
        return  f(account_data, *args, **kwargs)

    return decorated

def get_token():
    token = None
    if 'Authorization' in request.headers:
        auth_header = request.headers['Authorization'].split(' ')
        if len(auth_header) == 2 and auth_header[0] == 'Bearer':
            token = auth_header[1]
    return token
