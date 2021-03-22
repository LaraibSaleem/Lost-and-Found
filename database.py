import os
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#import mysqlconnector



#SQLALCHEMY_DATABASE_URL = os.getenv("mysql+pymysql://root://@<host>/lost_and_found")
#engine = create_engine(SQLALCHEMY_DATABASE_URL)

#engine = create_engine("mysql+pymysql://root:@<host>[3306]/lost_and_found")

engine = create_engine("mysql+pymysql://root@localhost/lost_and_found")

#print("***************ENGINE*************** =",engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()