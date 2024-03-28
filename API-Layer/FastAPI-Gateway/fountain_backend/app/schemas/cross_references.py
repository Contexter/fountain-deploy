from pydantic import BaseModel

class Cross_referencesBase(BaseModel):
    # Define common base attributes here

class Cross_referencesCreate(Cross_referencesBase):
    # Define creation-specific attributes here

class Cross_references(Cross_referencesBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
