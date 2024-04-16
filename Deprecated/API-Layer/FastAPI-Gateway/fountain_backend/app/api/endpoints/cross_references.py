from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import Cross_referencesCreate, Cross_references
from ...services import cross_references_service

router = APIRouter()

@router.post('/', response_model=Cross_references)
def create_cross_references(cross_references: Cross_referencesCreate, db: Session = Depends(get_db)):
    return cross_references_service.create_cross_references(db=db, cross_references=cross_references)

