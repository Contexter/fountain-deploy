from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import Section_headingCreate, Section_heading
from ...services import section_heading_service

router = APIRouter()

@router.post('/', response_model=Section_heading)
def create_section_heading(section_heading: Section_headingCreate, db: Session = Depends(get_db)):
    return section_heading_service.create_section_heading(db=db, section_heading=section_heading)

