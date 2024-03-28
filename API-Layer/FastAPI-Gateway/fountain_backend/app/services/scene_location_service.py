# Service layer for handling scene_location logic
from sqlalchemy.orm import Session
from ..schemas import Scene_locationCreate, Scene_location
from ..db.models import Scene_location

def create_scene_location(db: Session, scene_location: Scene_locationCreate):
    # Add service logic here

