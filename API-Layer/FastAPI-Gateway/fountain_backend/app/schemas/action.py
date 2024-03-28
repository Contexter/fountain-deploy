from pydantic import BaseModel

class ActionBase(BaseModel):
    # Define common base attributes here

class ActionCreate(ActionBase):
    # Define creation-specific attributes here

class Action(ActionBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
