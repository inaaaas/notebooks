@router.get("/laptops/search/")
def search_laptops(model: str, processor: str, db: Session = Depends(get_db)):
    return db.query(models.Laptop).filter(
        models.Laptop.model == model,
        models.Laptop.processor == processor
    ).all()
