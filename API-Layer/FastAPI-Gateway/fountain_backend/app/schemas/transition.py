from pydantic import BaseModel

class TransitionBase(BaseModel):
    # Define common base attributes here

class TransitionCreate(TransitionBase):
    # Define creation-specific attributes here

class Transition(TransitionBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
