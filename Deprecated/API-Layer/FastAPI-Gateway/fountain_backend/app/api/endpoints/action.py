from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import ActionCreate, Action
from ...services import action_service

router = APIRouter()

@router.post('/', response_model=Action)
def create_action(action: ActionCreate, db: Session = Depends(get_db)):
    return action_service.create_action(db=db, action=action)

