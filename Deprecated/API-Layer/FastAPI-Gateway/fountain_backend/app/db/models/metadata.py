from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Metadata(Base):
    __tablename__ = 'metadata'
    id = Column(Integer, primary_key=True, index=True)
