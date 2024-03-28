from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import MetadataCreate, Metadata
from ...services import metadata_service

router = APIRouter()

@router.post('/', response_model=Metadata)
def create_metadata(metadata: MetadataCreate, db: Session = Depends(get_db)):
    return metadata_service.create_metadata(db=db, metadata=metadata)

