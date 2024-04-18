from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Centered_text(Base):
    __tablename__ = 'centered_text'
    id = Column(Integer, primary_key=True, index=True)
