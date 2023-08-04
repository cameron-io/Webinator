from flask import request, jsonify
from model import Account
from functools import wraps
import jwt
from app import context

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
            return jsonify({'message': 'Token is missing'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, context.config['SECRET_KEY'])
            account_data = Account.query\
                .filter_by(public_id = data['public_id'])\
                .first()
        except:
            return jsonify({
                'message' : 'Token is invalid'
            }), 401
        # returns the current logged in account's context to the routes
        return  f(account_data, *args, **kwargs)
  
    return decorated
