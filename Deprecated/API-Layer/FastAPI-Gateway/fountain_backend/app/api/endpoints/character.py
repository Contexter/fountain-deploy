from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import CharacterCreate, Character
from ...services import character_service

router = APIRouter()

@router.post('/', response_model=Character)
def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    return character_service.create_character(db=db, character=character)

