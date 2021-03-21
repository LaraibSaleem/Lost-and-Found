#importing modules
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
#from fastapi.middleware.cors import CORSMiddleware

#importing other files of the app
#from . import models, schemas
import models, schemas
from app.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


'''
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
'''


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Home/welcome route
@app.get("/")
def read_root():
    return RedirectResponse(url="/docs/")


'''
# Get all items
@app.get("/items")
def get_items():
    return db

# get single item
@app.get("/items/{item_id}")
def get_a_item(item_id: int):
    item = item_id - 1
    return db[item]

# add a new item
@app.post("/items")
def add_item(item: Item):
    db.append(item.dict())
    return db[-1]

#update a item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    db[item_id-1] = item.dict()
    return db[item_id-1]

# delete a item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    db.remove(item_id-1)
    return {"task": "deletion successful"}
'''