from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import Scene_locationCreate, Scene_location
from ...services import scene_location_service

router = APIRouter()

@router.post('/', response_model=Scene_location)
def create_scene_location(scene_location: Scene_locationCreate, db: Session = Depends(get_db)):
    return scene_location_service.create_scene_location(db=db, scene_location=scene_location)

