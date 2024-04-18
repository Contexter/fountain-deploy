# Service layer for handling casting logic
from sqlalchemy.orm import Session
from ..schemas import CastingCreate, Casting
from ..db.models import Casting

def create_casting(db: Session, casting: CastingCreate):
    # Add service logic here

