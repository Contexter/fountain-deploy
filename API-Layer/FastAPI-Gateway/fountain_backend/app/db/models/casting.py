from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Casting(Base):
    __tablename__ = 'casting'
    id = Column(Integer, primary_key=True, index=True)
