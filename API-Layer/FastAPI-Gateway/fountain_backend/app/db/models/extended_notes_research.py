from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Extended_notes_research(Base):
    __tablename__ = 'extended_notes_research'
    id = Column(Integer, primary_key=True, index=True)
