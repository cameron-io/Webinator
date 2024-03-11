from sqlalchemy import Column, Integer, DateTime, String, Boolean, ForeignKey
from app import db

class Experience(db.Model):
    __tablename__ = 'experience'

    id = Column(Integer, primary_key = True)
    profile_id = Column(Integer, ForeignKey('profile.id'), nullable=False)
    title = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    location = Column(String(255))
    from_date = Column(DateTime(), nullable=False)
    to_date = Column(String(255))
    current = Column(Boolean, default=False)
    description = Column(String(255))
