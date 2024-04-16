from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import TransitionCreate, Transition
from ...services import transition_service

router = APIRouter()

@router.post('/', response_model=Transition)
def create_transition(transition: TransitionCreate, db: Session = Depends(get_db)):
    return transition_service.create_transition(db=db, transition=transition)

