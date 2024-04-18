from pydantic import BaseModel

class PropsBase(BaseModel):
    # Define common base attributes here

class PropsCreate(PropsBase):
    # Define creation-specific attributes here

class Props(PropsBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
