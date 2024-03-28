from pydantic import BaseModel

class Scene_locationBase(BaseModel):
    # Define common base attributes here

class Scene_locationCreate(Scene_locationBase):
    # Define creation-specific attributes here

class Scene_location(Scene_locationBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
