from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from database import Base


# user model to store users
class User(Base):
    __tablename__ = "User"

    id= Column(Integer, primary_key=True, autoincrement=True, index=True)
    uname= Column(String(255))
    pw= Column(String(255))