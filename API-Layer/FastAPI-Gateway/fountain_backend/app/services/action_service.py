# Service layer for handling action logic
from sqlalchemy.orm import Session
from ..schemas import ActionCreate, Action
from ..db.models import Action

def create_action(db: Session, action: ActionCreate):
    # Add service logic here

