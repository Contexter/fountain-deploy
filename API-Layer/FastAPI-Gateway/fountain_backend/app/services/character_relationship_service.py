# Service layer for handling character_relationship logic
from sqlalchemy.orm import Session
from ..schemas import Character_relationshipCreate, Character_relationship
from ..db.models import Character_relationship

def create_character_relationship(db: Session, character_relationship: Character_relationshipCreate):
    # Add service logic here

