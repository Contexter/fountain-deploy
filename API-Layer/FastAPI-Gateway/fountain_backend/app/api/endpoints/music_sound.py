from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...db.database import get_db
from ...schemas import Music_soundCreate, Music_sound
from ...services import music_sound_service

router = APIRouter()

@router.post('/', response_model=Music_sound)
def create_music_sound(music_sound: Music_soundCreate, db: Session = Depends(get_db)):
    return music_sound_service.create_music_sound(db=db, music_sound=music_sound)

