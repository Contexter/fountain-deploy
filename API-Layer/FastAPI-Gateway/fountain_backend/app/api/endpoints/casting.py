from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import CastingCreate, Casting
from ...services import casting_service

router = APIRouter()

@router.post('/', response_model=Casting)
def create_casting(casting: CastingCreate, db: Session = Depends(get_db)):
    return casting_service.create_casting(db=db, casting=casting)

