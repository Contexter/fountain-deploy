from pydantic import BaseModel

class Title_pageBase(BaseModel):
    # Define common base attributes here

class Title_pageCreate(Title_pageBase):
    # Define creation-specific attributes here

class Title_page(Title_pageBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
