from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from app import db

class Profile(db.Model):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key = True)
    account = Column(ForeignKey('account.id'))
    website = Column(String(255))
    location = Column(String(255))
    status = Column(String(255))
    skills = Column(String(255), nullable=False)
    bio = Column(String(255))
    githubusername = Column(String(255))
    experience = Column(db.relationship('experience', 'experience.profile_id'))
    Education = Column(db.relationship('experience', 'experience.profile_id'))
    social = Column(db.relationship('experience', 'experience.profile_id'))
    created_at = Column(DateTime)
