#importing modules
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
#from fastapi.middleware.cors import CORSMiddleware

#importing other files of the app
#from . import models, schemas
import models.item_model, models.user_model
from database import SessionLocal, engine
import schemas.item_schema, schemas.user_schema 
#password regex
import re

models.item_model.Base.metadata.create_all(bind=engine)
models.user_model.Base.metadata.create_all(bind=engine)

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
########## USER CRUD ##########
###############################

# sign up
@app.post("/users", response_model=List[schemas.user_schema.User])
def user_sign_up( user: schemas.user_schema.User, db: Session= Depends(get_db)):
    db_user = db.query(models.user_model.User).filter(models.user_model.User.uname == user.uname).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        #check pw regex
        # password regex
        reg = "^(.+[a-z])(.+[A-Z])(.+\d)(.+[\W])[\w\W]{8,20}$"
        # compiling regex
        reg_match = re.compile(reg)
        # checking regex
        res = re.search(reg_match, user.pw)
        if res:
            db_user2 = models.user_model.User(uname=user.uname, pw=user.pw)
            db.add(db_user2)
            db.commit()
            db.refresh(db_user2)
            return [db_user2]
        else:
            raise HTTPException(status_code=400, detail="Password too weak")



# log in
@app.get("/users", response_model=List[schemas.user_schema.User])
def user_log_in( uname: str, pw:str, db: Session= Depends(get_db)):
    db_user = db.query(models.user_model.User).filter(models.user_model.User.uname == uname,
                                                    models.user_model.User.pw == pw).one()
    if db_user:
        return [db_user]
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")




###############################
########## ITEM CRUD ##########
###############################

# get all items
@app.get("/items/", response_model=List[schemas.item_schema.Item])
def get_items(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    items = db.query(models.item_model.Item).offset(skip).limit(limit).all() #pagination added
    return items



# search item through name
@app.get("/items/{item_name}", response_model=List[schemas.item_schema.Item])
def search_item_by_name( item_name: str, db: Session= Depends(get_db)):
    item = db.query(models.item_model.Item).filter(models.item_model.Item.name == item_name).first()
    return [item]


# add a new item
@app.post("/items", response_model=List[schemas.item_schema.Item])
def add_items(item: schemas.item_schema.Item, db: Session= Depends(get_db)):
    db_item = models.item_model.Item(name=item.name, location=item.location, description=item.description, date=item.date)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return [db_item]


#update a item
@app.put("/items/{item_id}", response_model=List[schemas.item_schema.Item])
def update_items(item: schemas.item_schema.Item, db: Session= Depends(get_db)):
    db.query(models.item_model.Item).filter(models.item_model.Item.id==item.id).update({models.item_model.Item.name: item.name, models.item_model.Item.location: item.location})
    db.commit()
    db_item = db.query(models.item_model.Item).filter(models.item_model.Item.id==item.id).first()
    return [db_item]


# delete a item
@app.delete("/items/{item_id}", response_model=List[schemas.item_schema.Item])
def delete_item(item_id: int, db: Session= Depends(get_db)):
    db.query(models.item_model.Item).filter(models.item_model.Item.id == item_id).delete()
    db.commit()
    return {"Task": "Deletion Successful"}
#working fine
#check error 500 : internal server error
