from pydantic import BaseModel

class NoteBase(BaseModel):
    # Define common base attributes here

class NoteCreate(NoteBase):
    # Define creation-specific attributes here

class Note(NoteBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
