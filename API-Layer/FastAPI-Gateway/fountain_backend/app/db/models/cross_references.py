from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Cross_references(Base):
    __tablename__ = 'cross_references'
    id = Column(Integer, primary_key=True, index=True)
