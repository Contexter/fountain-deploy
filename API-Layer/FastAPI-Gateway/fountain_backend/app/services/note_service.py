# Service layer for handling note logic
from sqlalchemy.orm import Session
from ..schemas import NoteCreate, Note
from ..db.models import Note

def create_note(db: Session, note: NoteCreate):
    # Add service logic here

