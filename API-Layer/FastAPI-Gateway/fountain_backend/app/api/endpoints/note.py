from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import NoteCreate, Note
from ...services import note_service

router = APIRouter()

@router.post('/', response_model=Note)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    return note_service.create_note(db=db, note=note)

