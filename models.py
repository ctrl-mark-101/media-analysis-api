from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Media(BaseModel):
    id: int
    title: str
    type: str              # "book", "movie", "tv", "podcast", "game"
    genre: str
    rating: float
    created_at: Optional[datetime] = datetime.now()