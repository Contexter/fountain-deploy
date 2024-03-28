# Service layer for handling extended_notes_research logic
from sqlalchemy.orm import Session
from ..schemas import Extended_notes_researchCreate, Extended_notes_research
from ..db.models import Extended_notes_research

def create_extended_notes_research(db: Session, extended_notes_research: Extended_notes_researchCreate):
    # Add service logic here

