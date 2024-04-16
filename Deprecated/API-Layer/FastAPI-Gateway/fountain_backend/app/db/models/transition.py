from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Transition(Base):
    __tablename__ = 'transition'
    id = Column(Integer, primary_key=True, index=True)
