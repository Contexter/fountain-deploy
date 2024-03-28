from pydantic import BaseModel

class Formatting_rulesBase(BaseModel):
    # Define common base attributes here

class Formatting_rulesCreate(Formatting_rulesBase):
    # Define creation-specific attributes here

class Formatting_rules(Formatting_rulesBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
