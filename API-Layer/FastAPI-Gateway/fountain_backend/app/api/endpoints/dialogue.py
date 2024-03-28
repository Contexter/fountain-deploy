from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import DialogueCreate, Dialogue
from ...services import dialogue_service

router = APIRouter()

@router.post('/', response_model=Dialogue)
def create_dialogue(dialogue: DialogueCreate, db: Session = Depends(get_db)):
    return dialogue_service.create_dialogue(db=db, dialogue=dialogue)

