from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import ParentheticalCreate, Parenthetical
from ...services import parenthetical_service

router = APIRouter()

@router.post('/', response_model=Parenthetical)
def create_parenthetical(parenthetical: ParentheticalCreate, db: Session = Depends(get_db)):
    return parenthetical_service.create_parenthetical(db=db, parenthetical=parenthetical)

