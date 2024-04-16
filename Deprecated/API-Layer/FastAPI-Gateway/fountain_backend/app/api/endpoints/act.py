from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import ActCreate, Act
from ...services import act_service

router = APIRouter()

@router.post('/', response_model=Act)
def create_act(act: ActCreate, db: Session = Depends(get_db)):
    return act_service.create_act(db=db, act=act)

