import uuid
from werkzeug.security import generate_password_hash

from app import db

from models.account import Account

def get_user_by_email(user_email):
    return Account.query\
        .filter_by(email = user_email)\
        .first()

def get_user_by_public_id(public_id):
    return Account.query\
                .filter_by(public_id = public_id)\
                .first()

def create_user_account(username, email, password):
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
