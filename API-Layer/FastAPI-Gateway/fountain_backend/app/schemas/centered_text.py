from pydantic import BaseModel

class Centered_textBase(BaseModel):
    # Define common base attributes here

class Centered_textCreate(Centered_textBase):
    # Define creation-specific attributes here

class Centered_text(Centered_textBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
