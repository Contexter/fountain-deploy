from pydantic import BaseModel

class SceneBase(BaseModel):
    # Define common base attributes here

class SceneCreate(SceneBase):
    # Define creation-specific attributes here

class Scene(SceneBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
