from pydantic import BaseModel

class PlaywrightBase(BaseModel):
    # Define common base attributes here

class PlaywrightCreate(PlaywrightBase):
    # Define creation-specific attributes here

class Playwright(PlaywrightBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
