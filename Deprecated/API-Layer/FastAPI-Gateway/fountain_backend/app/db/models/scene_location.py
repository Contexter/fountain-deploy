from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Scene_location(Base):
    __tablename__ = 'scene_location'
    id = Column(Integer, primary_key=True, index=True)
