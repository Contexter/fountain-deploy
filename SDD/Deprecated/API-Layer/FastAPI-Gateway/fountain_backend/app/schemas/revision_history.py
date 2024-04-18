from pydantic import BaseModel

class Revision_historyBase(BaseModel):
    # Define common base attributes here

class Revision_historyCreate(Revision_historyBase):
    # Define creation-specific attributes here

class Revision_history(Revision_historyBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
