# Service layer for handling playwright logic
from sqlalchemy.orm import Session
from ..schemas import PlaywrightCreate, Playwright
from ..db.models import Playwright

def create_playwright(db: Session, playwright: PlaywrightCreate):
    # Add service logic here

