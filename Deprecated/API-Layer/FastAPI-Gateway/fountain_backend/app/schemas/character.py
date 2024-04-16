from pydantic import BaseModel

class CharacterBase(BaseModel):
    # Define common base attributes here

class CharacterCreate(CharacterBase):
    # Define creation-specific attributes here

class Character(CharacterBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
