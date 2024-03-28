from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import PropsCreate, Props
from ...services import props_service

router = APIRouter()

@router.post('/', response_model=Props)
def create_props(props: PropsCreate, db: Session = Depends(get_db)):
    return props_service.create_props(db=db, props=props)

