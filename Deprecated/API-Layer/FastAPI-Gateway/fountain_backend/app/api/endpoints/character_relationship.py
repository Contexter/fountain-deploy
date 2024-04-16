from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import Character_relationshipCreate, Character_relationship
from ...services import character_relationship_service

router = APIRouter()

@router.post('/', response_model=Character_relationship)
def create_character_relationship(character_relationship: Character_relationshipCreate, db: Session = Depends(get_db)):
    return character_relationship_service.create_character_relationship(db=db, character_relationship=character_relationship)

