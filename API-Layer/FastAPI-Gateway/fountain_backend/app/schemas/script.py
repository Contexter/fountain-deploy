from pydantic import BaseModel

class ScriptBase(BaseModel):
    # Define common base attributes here

class ScriptCreate(ScriptBase):
    # Define creation-specific attributes here

class Script(ScriptBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
