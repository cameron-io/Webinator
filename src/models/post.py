from sqlalchemy import Column, Integer
from app import db

class Post(db.Model):
    id = Column(Integer, primary_key = True)
