from datetime import date
from pydantic import BaseModel



# user schema to store users
class User(BaseModel):
    id: int
    uname: str
    pw: str  

    class Config:
        orm_mode = True
