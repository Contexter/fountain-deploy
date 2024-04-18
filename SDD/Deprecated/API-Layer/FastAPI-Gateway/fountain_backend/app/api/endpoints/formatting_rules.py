from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import Formatting_rulesCreate, Formatting_rules
from ...services import formatting_rules_service

router = APIRouter()

@router.post('/', response_model=Formatting_rules)
def create_formatting_rules(formatting_rules: Formatting_rulesCreate, db: Session = Depends(get_db)):
    return formatting_rules_service.create_formatting_rules(db=db, formatting_rules=formatting_rules)

