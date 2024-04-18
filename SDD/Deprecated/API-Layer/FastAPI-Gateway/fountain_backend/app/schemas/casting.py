from pydantic import BaseModel

class CastingBase(BaseModel):
    # Define common base attributes here

class CastingCreate(CastingBase):
    # Define creation-specific attributes here

class Casting(CastingBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
