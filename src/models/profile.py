from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from app import db

class Profile(db.Model):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key = True)
    account_id = Column(Integer, ForeignKey('account.id'), nullable=False)
    website = Column(String(255))
    location = Column(String(255))
    status = Column(String(255))
    skills = Column(String(255), nullable=False)
    bio = Column(String(255))
    githubusername = Column(String(255))
    experience = db.relationship('Experience', backref='profile', lazy=True)
    Education = db.relationship('Education', backref='profile', lazy=True)
    social = db.relationship('Social', backref='profile', lazy=True)
    created_at = Column(DateTime)
