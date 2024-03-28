from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import Extended_notes_researchCreate, Extended_notes_research
from ...services import extended_notes_research_service

router = APIRouter()

@router.post('/', response_model=Extended_notes_research)
def create_extended_notes_research(extended_notes_research: Extended_notes_researchCreate, db: Session = Depends(get_db)):
    return extended_notes_research_service.create_extended_notes_research(db=db, extended_notes_research=extended_notes_research)

