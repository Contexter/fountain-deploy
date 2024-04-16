from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import ScriptCreate, Script
from ...services import script_service

router = APIRouter()

@router.post('/', response_model=Script)
def create_script(script: ScriptCreate, db: Session = Depends(get_db)):
    return script_service.create_script(db=db, script=script)

