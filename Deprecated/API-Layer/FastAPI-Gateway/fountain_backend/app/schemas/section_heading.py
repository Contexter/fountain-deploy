from pydantic import BaseModel

class Section_headingBase(BaseModel):
    # Define common base attributes here

class Section_headingCreate(Section_headingBase):
    # Define creation-specific attributes here

class Section_heading(Section_headingBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
