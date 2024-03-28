# Service layer for handling script logic
from sqlalchemy.orm import Session
from ..schemas import ScriptCreate, Script
from ..db.models import Script

def create_script(db: Session, script: ScriptCreate):
    # Add service logic here

