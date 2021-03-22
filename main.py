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
from database import SessionLocal, engine


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
    #return {"greeting":"Hello World!"}


###############################
########## ITEM CRUD ##########
###############################

# get all items
@app.get("/items/", response_model=List[schemas.Item])
def get_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items


# get single item
@app.get("/items/{item_id}", response_model=List[schemas.Item])
def get_a_item( item_id: int, db: Session= Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    return item


# add a new item
@app.post("/items", response_model=List[schemas.Item])
def add_items(item: schemas.Item, db: Session= Depends(get_db)):
    db_item = models.Item(name=item.name, location=item.location, description=item.description, date=item.date)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    #return db_item
    #return {"Success": "db_item"}
    return {"Task": "Addition Successful"}
#working fine
#check error 500 : internal server error


#update a item
@app.put("/items/{item_id}", response_model=List[schemas.Item])
def update_items(item: schemas.Item, db: Session= Depends(get_db)):
    db.query(models.Item).filter(models.Item.id==item.id).update({models.Item.name: item.name, models.Item.location: item.location})
    db.commit()
    db_item = db.query(models.Item).filter(models.Item.id==item.id).first()
    #return db_item
    #return {"Success": "db_item"}
    return {"Task": "Updation Successful"}
#working fine
#check error 500 : internal server error


# delete a item
@app.delete("/items/{item_id}", response_model=List[schemas.Item])
def delete_item(item_id: int, db: Session= Depends(get_db)):
    db.query(models.Item).filter(models.Item.id == item_id).delete()
    db.commit()
    return {"Task": "Deletion Successful"}
#working fine
#check error 500 : internal server error