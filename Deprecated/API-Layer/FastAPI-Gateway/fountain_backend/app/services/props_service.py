# Service layer for handling props logic
from sqlalchemy.orm import Session
from ..schemas import PropsCreate, Props
from ..db.models import Props

def create_props(db: Session, props: PropsCreate):
    # Add service logic here

