from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import Centered_textCreate, Centered_text
from ...services import centered_text_service

router = APIRouter()

@router.post('/', response_model=Centered_text)
def create_centered_text(centered_text: Centered_textCreate, db: Session = Depends(get_db)):
    return centered_text_service.create_centered_text(db=db, centered_text=centered_text)

