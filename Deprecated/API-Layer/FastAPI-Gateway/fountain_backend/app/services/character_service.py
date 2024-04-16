# Service layer for handling character logic
from sqlalchemy.orm import Session
from ..schemas import CharacterCreate, Character
from ..db.models import Character

def create_character(db: Session, character: CharacterCreate):
    # Add service logic here

