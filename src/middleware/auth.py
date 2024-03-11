from flask import request
from functools import wraps
import jwt
from app import app
from service.user import get_user_by_public_id

# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies['token']
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
