from flask import request
from model import Account
from functools import wraps
import jwt
from app import app

# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]
        # return 401 if token is not passed
        if not token:
            return ({'message': 'Token is missing'}, 401)
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'])
            account_data = Account.query\
                .filter_by(public_id = data['public_id'])\
                .first()
        except:
            return ('', 401)
        # returns the current logged in account's context to the routes
        return  f(account_data, *args, **kwargs)
  
    return decorated
