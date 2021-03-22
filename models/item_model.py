from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from database import Base


# item model to store items
class Item(Base):
    __tablename__ = "Item"

    id= Column(Integer, primary_key=True, autoincrement=True, index=True)
    name= Column(String(255))
    location= Column(String(255))
    description= Column(String(255))
    date = Column(Date)  
    #pic:  


