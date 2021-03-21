import csv
import datetime
import models
from database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

with open("Item.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        db_record = models.Item(
            id=row["id"],
            name=row["name"],
            location=row["location"],
            description=row["description"],
            date=datetime.datetime.strptime(row["date"], "%Y-%m-%d"),
            #pic=row["pic"],
        )
        db.add(db_record)

    db.commit()

db.close()
