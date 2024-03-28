from pydantic import BaseModel

class Page_breakBase(BaseModel):
    # Define common base attributes here

class Page_breakCreate(Page_breakBase):
    # Define creation-specific attributes here

class Page_break(Page_breakBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
