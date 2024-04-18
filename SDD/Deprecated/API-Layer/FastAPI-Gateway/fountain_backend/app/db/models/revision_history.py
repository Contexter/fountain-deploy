from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Revision_history(Base):
    __tablename__ = 'revision_history'
    id = Column(Integer, primary_key=True, index=True)
