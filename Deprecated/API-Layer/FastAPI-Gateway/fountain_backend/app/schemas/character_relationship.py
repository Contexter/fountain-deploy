from pydantic import BaseModel

class Character_relationshipBase(BaseModel):
    # Define common base attributes here

class Character_relationshipCreate(Character_relationshipBase):
    # Define creation-specific attributes here

class Character_relationship(Character_relationshipBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
