from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import Revision_historyCreate, Revision_history
from ...services import revision_history_service

router = APIRouter()

@router.post('/', response_model=Revision_history)
def create_revision_history(revision_history: Revision_historyCreate, db: Session = Depends(get_db)):
    return revision_history_service.create_revision_history(db=db, revision_history=revision_history)

