from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import Title_pageCreate, Title_page
from ...services import title_page_service

router = APIRouter()

@router.post('/', response_model=Title_page)
def create_title_page(title_page: Title_pageCreate, db: Session = Depends(get_db)):
    return title_page_service.create_title_page(db=db, title_page=title_page)

