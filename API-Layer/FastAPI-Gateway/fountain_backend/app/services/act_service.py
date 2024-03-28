# Service layer for handling act logic
from sqlalchemy.orm import Session
from ..schemas import ActCreate, Act
from ..db.models import Act

def create_act(db: Session, act: ActCreate):
    # Add service logic here

