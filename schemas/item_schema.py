from datetime import date
from pydantic import BaseModel



# item schema to store items
class Item(BaseModel):
    id: int
    name: str
    location: str
    description: str
    date: date
    #pic:  

    class Config:
        orm_mode = True