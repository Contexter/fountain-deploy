from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import Page_breakCreate, Page_break
from ...services import page_break_service

router = APIRouter()

@router.post('/', response_model=Page_break)
def create_page_break(page_break: Page_breakCreate, db: Session = Depends(get_db)):
    return page_break_service.create_page_break(db=db, page_break=page_break)

