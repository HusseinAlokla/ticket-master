from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventSchema(BaseModel):
    id: str
    name: str
    date: Optional[datetime] = None
    image_url: Optional[str] = None
    venue: Optional[str] = None

    class Config:
        orm_mode = True