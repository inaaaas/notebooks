@router.put("/laptops/update_processor/")
def update_processor(memory_size: int, new_processor: str, db: Session = Depends(get_db)):
    db.query(models.Laptop).filter(models.Laptop.memory_size == memory_size).update(
        {"processor": new_processor}, synchronize_session=False
    )
    db.commit()
    return {"message": "Processor updated"}
