@router.put("/laptops/{laptop_id}/extra_specs/")
def add_extra_specs(laptop_id: int, specs: dict, db: Session = Depends(get_db)):
    laptop = db.query(models.Laptop).filter(models.Laptop.id == laptop_id).first()
    laptop.extra_specs = specs
    db.commit()
    return {"message": "Extra specs added"}
