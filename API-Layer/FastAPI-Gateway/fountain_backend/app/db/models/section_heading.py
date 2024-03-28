from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Section_heading(Base):
    __tablename__ = 'section_heading'
    id = Column(Integer, primary_key=True, index=True)
