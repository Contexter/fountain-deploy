from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import PlaywrightCreate, Playwright
from ...services import playwright_service

router = APIRouter()

@router.post('/', response_model=Playwright)
def create_playwright(playwright: PlaywrightCreate, db: Session = Depends(get_db)):
    return playwright_service.create_playwright(db=db, playwright=playwright)

