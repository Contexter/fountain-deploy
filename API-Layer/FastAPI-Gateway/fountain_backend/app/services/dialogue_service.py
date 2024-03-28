# Service layer for handling dialogue logic
from sqlalchemy.orm import Session
from ..schemas import DialogueCreate, Dialogue
from ..db.models import Dialogue

def create_dialogue(db: Session, dialogue: DialogueCreate):
    # Add service logic here

