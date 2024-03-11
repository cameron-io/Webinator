from sqlalchemy import Column, Integer, String, ForeignKey
from app import db

class Social(db.Model):
    id = Column(Integer, primary_key = True)
    profile_id = Column(ForeignKey('profile.id'))
    youtube = Column(String(255))
    twitter = Column(String(255))
    facebook = Column(String(255))
    linkedin = Column(String(255))
    instagram = Column(String(255))
