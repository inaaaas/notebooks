from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/laptops/", response_model=schemas.Laptop)
def create_laptop(laptop: schemas.LaptopCreate, db: Session = Depends(get_db)):
    return crud.create_laptop(db=db, laptop=laptop)

@router.get("/laptops/", response_model=list[schemas.Laptop])
def read_laptops(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_laptops(db, skip=skip, limit=limit)

@router.get("/laptops/{laptop_id}", response_model=schemas.Laptop)
def read_laptop(laptop_id: int, db: Session = Depends(get_db)):
    db_laptop = crud.get_laptop(db, laptop_id=laptop_id)
    if db_laptop is None:
        raise HTTPException(status_code=404, detail="Laptop not found")
    return db_laptop

@router.delete("/laptops/{laptop_id}")
def delete_laptop(laptop_id: int, db: Session = Depends(get_db)):
    crud.delete_laptop(db, laptop_id=laptop_id)
    return {"message": "Laptop deleted"}
