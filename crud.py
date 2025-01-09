from sqlalchemy.orm import Session
from . import models, schemas

def create_laptop(db: Session, laptop: schemas.LaptopCreate):
    db_laptop = models.Laptop(**laptop.dict())
    db.add(db_laptop)
    db.commit()
    db.refresh(db_laptop)
    return db_laptop

def get_laptops(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Laptop).offset(skip).limit(limit).all()

def get_laptop(db: Session, laptop_id: int):
    return db.query(models.Laptop).filter(models.Laptop.id == laptop_id).first()

def delete_laptop(db: Session, laptop_id: int):
    db_laptop = db.query(models.Laptop).filter(models.Laptop.id == laptop_id).first()
    if db_laptop:
        db.delete(db_laptop)
        db.commit()
