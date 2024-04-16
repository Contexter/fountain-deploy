# Service layer for handling centered_text logic
from sqlalchemy.orm import Session
from ..schemas import Centered_textCreate, Centered_text
from ..db.models import Centered_text

def create_centered_text(db: Session, centered_text: Centered_textCreate):
    # Add service logic here

