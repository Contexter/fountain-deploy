from pydantic import BaseModel

class ActBase(BaseModel):
    # Define common base attributes here

class ActCreate(ActBase):
    # Define creation-specific attributes here

class Act(ActBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
