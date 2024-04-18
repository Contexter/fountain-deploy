from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Scene(Base):
    __tablename__ = 'scene'
    id = Column(Integer, primary_key=True, index=True)
