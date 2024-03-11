from sqlalchemy import Column, Integer, String
from app import db

class Account(db.Model):
    __tablename__ = 'account'

    id = Column(Integer, primary_key = True)
    public_id = Column(String(50), unique = True)
    username = Column(String(100))
    email = Column(String(70), unique = True)
    password = Column(String(255))
    profile = db.relationship('Profile', backref='account', lazy=True)

    def __repr__(self):
        return '<Account %r>' % self.username
