from pydantic import BaseModel

class ParentheticalBase(BaseModel):
    # Define common base attributes here

class ParentheticalCreate(ParentheticalBase):
    # Define creation-specific attributes here

class Parenthetical(ParentheticalBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
