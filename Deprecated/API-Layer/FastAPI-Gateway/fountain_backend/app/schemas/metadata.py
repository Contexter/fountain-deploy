from pydantic import BaseModel

class MetadataBase(BaseModel):
    # Define common base attributes here

class MetadataCreate(MetadataBase):
    # Define creation-specific attributes here

class Metadata(MetadataBase):
    id: int
    # Define additional attributes here

    class Config:
        orm_mode = True
