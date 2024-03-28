# Service layer for handling parenthetical logic
from sqlalchemy.orm import Session
from ..schemas import ParentheticalCreate, Parenthetical
from ..db.models import Parenthetical

def create_parenthetical(db: Session, parenthetical: ParentheticalCreate):
    # Add service logic here

