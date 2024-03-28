from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Formatting_rules(Base):
    __tablename__ = 'formatting_rules'
    id = Column(Integer, primary_key=True, index=True)
