from pydantic import BaseModel

class Extended_notes_researchBase(BaseModel):
    # Define common base attributes here

class Extended_notes_researchCreate(Extended_notes_researchBase):
    # Define creation-specific attributes here

class Extended_notes_research(Extended_notes_researchBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
