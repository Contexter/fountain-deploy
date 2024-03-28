from pydantic import BaseModel

class Music_soundBase(BaseModel):
    # Define common base attributes here

class Music_soundCreate(Music_soundBase):
    # Define creation-specific attributes here

class Music_sound(Music_soundBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
