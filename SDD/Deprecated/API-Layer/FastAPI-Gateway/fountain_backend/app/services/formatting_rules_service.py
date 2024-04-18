# Service layer for handling formatting_rules logic
from sqlalchemy.orm import Session
from ..schemas import Formatting_rulesCreate, Formatting_rules
from ..db.models import Formatting_rules

def create_formatting_rules(db: Session, formatting_rules: Formatting_rulesCreate):
    # Add service logic here

