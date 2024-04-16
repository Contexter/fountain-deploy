from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Character_relationship(Base):
    __tablename__ = 'character_relationship'
    id = Column(Integer, primary_key=True, index=True)
