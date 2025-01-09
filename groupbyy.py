from sqlalchemy import func

@router.get("/manufacturers/group_by_country/")
def group_by_country(db: Session = Depends(get_db)):
    return db.query(
        models.Manufacturer.country, func.count(models.Manufacturer.id).label("manufacturer_count")
    ).group_by(models.Manufacturer.country).all()
