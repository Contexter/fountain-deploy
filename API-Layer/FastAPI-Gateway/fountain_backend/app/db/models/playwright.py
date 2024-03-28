from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Playwright(Base):
    __tablename__ = 'playwright'
    id = Column(Integer, primary_key=True, index=True)
