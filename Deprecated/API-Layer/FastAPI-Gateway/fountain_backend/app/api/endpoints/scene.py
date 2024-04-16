from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import SceneCreate, Scene
from ...services import scene_service

router = APIRouter()

@router.post('/', response_model=Scene)
def create_scene(scene: SceneCreate, db: Session = Depends(get_db)):
    return scene_service.create_scene(db=db, scene=scene)

