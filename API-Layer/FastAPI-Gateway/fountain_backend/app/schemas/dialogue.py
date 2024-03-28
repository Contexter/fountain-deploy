from pydantic import BaseModel

class DialogueBase(BaseModel):
    # Define common base attributes here

class DialogueCreate(DialogueBase):
    # Define creation-specific attributes here

class Dialogue(DialogueBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
