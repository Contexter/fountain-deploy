from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Page_break(Base):
    __tablename__ = 'page_break'
    id = Column(Integer, primary_key=True, index=True)
