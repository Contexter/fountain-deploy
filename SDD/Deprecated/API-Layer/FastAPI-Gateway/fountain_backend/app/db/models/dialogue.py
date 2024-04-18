from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Dialogue(Base):
    __tablename__ = 'dialogue'
    id = Column(Integer, primary_key=True, index=True)
