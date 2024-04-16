from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Title_page(Base):
    __tablename__ = 'title_page'
    id = Column(Integer, primary_key=True, index=True)
